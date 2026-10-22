"""Remove GPQA-Diamond item text from the released artifacts, in place.

Why this exists
---------------
GPQA-Diamond is distributed under terms that ask consumers not to reveal examples in
plain text, to keep the benchmark out of training corpora. The pipeline needs the item
text to run; the release does not. This script rewrites the committed artifacts so they
carry identifiers, answer letters, verdicts and metrics, but no question text, no option
strings and no model prose.

The release therefore keeps every number reproducible while shipping none of the
benchmark's content. Reconstructing the items is a documented, token-gated step:
`python src/data_loader.py --mode actual --domain science` with HF_TOKEN set.

Run this before every commit that touches data/ or reports/. It is idempotent.

Usage
-----
    python src/redact_release.py            # redact in place
    python src/redact_release.py --check    # verify only; exit 1 on any leak
"""
import argparse
import csv
import json
import os
import sys

from science_utils import SCIENCE_WITHHELD_PLACEHOLDER as WITHHELD
from verdict_utils import recover_verdict_from_raw_response

SCIENCE_FIELDS_TO_DROP = ("options", "option_map", "correct_answer_text")
VERIFIED_TEXT_FIELDS = ("raw_response", "thinking_or_evaluation", "candidate_answer_text")
PROBE_TEXT_FIELDS = ("original_text", "mistral_text", "control_text")

RAW = os.path.join("data", "raw")
GENERATED = os.path.join("data", "generated")
VERIFIED = os.path.join("data", "verified")


def _read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def _write_jsonl(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def _redact_item_text(item):
    """Replace question text with the placeholder and drop every option-bearing field."""
    for key in ("question", "question_stem"):
        if key in item:
            item[key] = WITHHELD
    for key in SCIENCE_FIELDS_TO_DROP:
        item.pop(key, None)
    return item


def redact_raw(path):
    rows = [_redact_item_text(item) for item in _read_jsonl(path)]
    _write_jsonl(path, rows)
    return len(rows)


def redact_generated(path):
    rows = []
    for item in _read_jsonl(path):
        item = _redact_item_text(item)
        candidates = item.get("candidates") or {}
        item["candidates"] = {m: (WITHHELD if v else None) for m, v in candidates.items()}
        rows.append(item)
    _write_jsonl(path, rows)
    return len(rows)


def redact_verified(path):
    rows = []
    for row in _read_jsonl(path):
        thinking = row.get("thinking_or_evaluation")
        if "verbosity_chars" not in row:
            row["verbosity_chars"] = len(thinking) if isinstance(thinking, str) else 0
        # Preserve the verdict-recovery decision that report.py would otherwise re-derive
        # from the raw response, which is about to be masked.
        if row.get("parsed_verdict") is None and "verdict_recovered" not in row:
            row["verdict_recovered"] = recover_verdict_from_raw_response(row.get("raw_response"))
        for key in VERIFIED_TEXT_FIELDS:
            if row.get(key) is not None:
                row[key] = WITHHELD
        rows.append(row)
    _write_jsonl(path, rows)
    return len(rows)


def redact_probe_traces(reports_dir):
    """Mask the science rows of the probe traces that reproduce candidate text."""
    touched = {}
    probes_dir = os.path.join(reports_dir, "probes")
    if not os.path.isdir(probes_dir):
        return touched
    for root, _, files in os.walk(probes_dir):
        for name in files:
            if not name.endswith(".jsonl"):
                continue
            path = os.path.join(root, name)
            rows = list(_read_jsonl(path))
            changed = 0
            for row in rows:
                if row.get("domain") != "science":
                    continue
                for key in PROBE_TEXT_FIELDS:
                    if isinstance(row.get(key), str) and row[key]:
                        row[key] = WITHHELD
                        changed += 1
            if changed:
                _write_jsonl(path, rows)
                touched[os.path.relpath(path)] = changed
    return touched


def redact_report_csvs(reports_dir):
    """Blank the option-bearing columns of the committed report CSVs."""
    touched = {}
    for root, _, files in os.walk(reports_dir):
        if os.path.basename(root) == "probes" or f"{os.sep}probes{os.sep}" in root:
            continue
        for name in files:
            if not name.endswith(".csv"):
                continue
            path = os.path.join(root, name)
            with open(path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or []
                rows = list(reader)
            targets = [c for c in ("ground_truth_text", "extracted_option_text") if c in fieldnames]
            if targets:
                for row in rows:
                    for col in targets:
                        row[col] = ""
            if "candidate_answer_text" in fieldnames:
                for row in rows:
                    # Only mask text that exists. An empty cell means the parser extracted
                    # nothing, which is a real result and must stay distinguishable from
                    # "withheld at release".
                    if row.get("domain") == "science" and row.get("candidate_answer_text"):
                        row["candidate_answer_text"] = WITHHELD
            if targets or "candidate_answer_text" in fieldnames:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                touched[os.path.relpath(path)] = len(rows)
    return touched


def _science_files(root, suffix):
    path = os.path.join(root, f"science{suffix}")
    return path if os.path.exists(path) else None


def redact(data_dir, reports_dir):
    summary = {}
    for suffix in (".jsonl", "_pilot.jsonl"):
        raw = _science_files(os.path.join(data_dir, "raw"), suffix)
        gen = _science_files(os.path.join(data_dir, "generated"), suffix)
        ver = _science_files(os.path.join(data_dir, "verified"), suffix)
        if raw:
            summary[f"raw{suffix}"] = redact_raw(raw)
        if gen:
            summary[f"generated{suffix}"] = redact_generated(gen)
        if ver:
            summary[f"verified{suffix}"] = redact_verified(ver)
    summary.update(redact_probe_traces(reports_dir))
    summary.update(redact_report_csvs(reports_dir))
    return summary


def check(data_dir, reports_dir):
    """Return a list of (path, problem) for anything that still carries item text."""
    problems = []
    for suffix in (".jsonl", "_pilot.jsonl"):
        for kind, fields in (
            ("raw", SCIENCE_FIELDS_TO_DROP),
            ("generated", SCIENCE_FIELDS_TO_DROP),
        ):
            path = _science_files(os.path.join(data_dir, kind), suffix)
            if not path:
                continue
            for row in _read_jsonl(path):
                for field in fields:
                    if field in row:
                        problems.append((path, f"{row.get('item_id')} still has '{field}'"))
                for field in ("question", "question_stem"):
                    if field in row and not (isinstance(row[field], str) and "[WITHHELD" in row[field]):
                        problems.append((path, f"{row.get('item_id')} still has '{field}'"))
                for model, value in (row.get("candidates") or {}).items():
                    if isinstance(value, str) and "[WITHHELD" not in value:
                        problems.append((path, f"{row.get('item_id')}/{model} candidate text"))
        ver = _science_files(os.path.join(data_dir, "verified"), suffix)
        if ver:
            for row in _read_jsonl(ver):
                for field in VERIFIED_TEXT_FIELDS:
                    value = row.get(field)
                    if isinstance(value, str) and value and "[WITHHELD" not in value:
                        problems.append((ver, f"{row.get('item_id')} still has '{field}'"))
                if row.get("verbosity_chars") is None:
                    problems.append((ver, f"{row.get('item_id')} missing verbosity_chars"))
    probes = os.path.join(reports_dir, "probes")
    if os.path.isdir(probes):
        for root, _, files in os.walk(probes):
            for name in files:
                if not name.endswith(".jsonl"):
                    continue
                path = os.path.join(root, name)
                for row in _read_jsonl(path):
                    if row.get("domain") != "science":
                        continue
                    for field in PROBE_TEXT_FIELDS:
                        value = row.get(field)
                        if isinstance(value, str) and value and "[WITHHELD" not in value:
                            problems.append((path, f"{row.get('item_id')} still has '{field}'"))
    for root, _, files in os.walk(reports_dir):
        if f"{os.sep}probes{os.sep}" in root:
            continue
        for name in files:
            if not name.endswith(".csv"):
                continue
            path = os.path.join(root, name)
            with open(path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or []
                for row in reader:
                    for col in ("ground_truth_text", "extracted_option_text"):
                        if col in fieldnames and row.get(col):
                            problems.append((path, f"non-empty '{col}'"))
                    text = row.get("candidate_answer_text")
                    if text and row.get("domain") == "science" and "[WITHHELD" not in text:
                        problems.append((path, "science row with candidate_answer_text"))
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--check", action="store_true", help="Verify only; exit 1 on any leak")
    args = parser.parse_args()

    if args.check:
        problems = check(args.data_dir, args.reports_dir)
        if problems:
            print(f"FAIL: {len(problems)} leaked field(s) in released artifacts")
            for path, problem in problems[:20]:
                print(f"  {path}: {problem}")
            sys.exit(1)
        print("OK: no GPQA-Diamond question text or option strings in released artifacts")
        return

    summary = redact(args.data_dir, args.reports_dir)
    for name, count in summary.items():
        print(f"redacted {count:>6} record(s) in {name}")
    problems = check(args.data_dir, args.reports_dir)
    if problems:
        print(f"WARNING: {len(problems)} field(s) still look unredacted")
        sys.exit(1)
    print("OK: release is clean")


if __name__ == "__main__":
    main()
