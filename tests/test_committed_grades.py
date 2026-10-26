"""
Reports must agree with the committed grades.

report.py reads code correctness from the committed probe cache instead of re-running the
candidates, because candidates near the 5 s execution timeout pass on one machine and time
out on another. The probe reports drop pairs that a regrade showed are no longer wrong.
These tests fail if either drifts from the committed grades.
"""
import csv
import json
import os
import sys
import unittest
from types import SimpleNamespace
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

import report  # noqa: E402

PROBES = os.path.join(ROOT, "reports", "probes")
GRADES_DIR = os.path.join(PROBES, "Do-stronger-models-make-mistakes-that-are-harder-to-catch")


def _grades(domain):
    with open(os.path.join(GRADES_DIR, f"graded_{domain}.json"), encoding="utf-8") as f:
        return json.load(f)


def _jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class CodeLabelsAreFrozen(unittest.TestCase):
    def test_committed_labels_cover_every_code_candidate(self):
        generated = _jsonl(os.path.join(ROOT, "data", "generated", "code.jsonl"))
        keys = {f"{row['item_id']}|{gen}" for row in generated for gen in row["candidates"]}
        self.assertEqual(keys, set(_grades("code")))

    def test_report_reads_code_labels_instead_of_executing(self):
        args = SimpleNamespace(
            raw_dir=os.path.join(ROOT, "data", "raw"),
            gen_dir=os.path.join(ROOT, "data", "generated"),
            ver_dir=os.path.join(ROOT, "data", "verified"),
            mode="actual",
            domains=["code"],
        )
        cwd = os.getcwd()
        os.chdir(ROOT)  # report.py resolves the label file relative to the repository root
        try:
            with mock.patch.object(report, "grade_code", side_effect=AssertionError("code was re-executed")):
                graded, _ = report.load_and_grade(args)
        finally:
            os.chdir(cwd)
        expected = {("code", *key.split("|")): ok for key, ok in _grades("code").items()}
        self.assertEqual(graded, expected)


class ProbeReportsMatchGrades(unittest.TestCase):
    def setUp(self):
        self.grades = {}
        for domain in ("code", "math", "science"):
            self.grades.update(_grades(domain))

    def test_self_preference_report_counts_each_still_wrong_item_once(self):
        traces = _jsonl(os.path.join(PROBES, "structural_self_preference", "self_preference_traces.jsonl"))
        kept = {t["item_id"] for t in traces
                if not self.grades[f"{t['item_id']}|deepseek"] and not self.grades[f"{t['item_id']}|qwen"]}
        rows = _csv(os.path.join(PROBES, "structural_self_preference", "self_preference_domain_breakdown.csv"))
        totals = [int(row["Items"]) for row in rows if row["Domain"] == "ALL"]
        self.assertEqual(totals, [len(kept), len(kept)])

    def test_style_transfer_report_drops_answers_now_graded_correct(self):
        traces = _jsonl(os.path.join(PROBES, "style_transfer", "style_transfer_traces.jsonl"))
        for row in _csv(os.path.join(PROBES, "style_transfer", "style_transfer_breakdown.csv")):
            verifier = row["Verifier"].lower()
            kept = [t for t in traces
                    if t["verifier"] == verifier and not self.grades[f"{t['item_id']}|{verifier}"]]
            self.assertEqual(int(row["Total False Positives Tested"]), len(kept), verifier)


if __name__ == "__main__":
    unittest.main(verbosity=2)
