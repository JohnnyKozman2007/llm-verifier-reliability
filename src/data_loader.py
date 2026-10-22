import os
import json
import random
import subprocess
from datasets import load_dataset
from dotenv import load_dotenv
from science_utils import build_option_map, render_science_question, validate_science_options

load_dotenv()

RAW_DATA_DIR = os.path.join("data", "raw")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Marker written by the public-release redaction (PR #6 onwards). Question text keeps
# its own placeholder even for licensed users; this one marks option/answer text.
OPTION_PLACEHOLDER = "[WITHHELD: GPQA-Diamond option text]"

def load_math(mode):
    print("Loading MATH dataset...")
    # MATH dataset 'dim/competition_math' only has a train split.
    ds = load_dataset('dim/competition_math', split='train')
    
    num_samples = 10 if mode == "pilot" else 150
    sampled = ds.shuffle(seed=42).select(range(num_samples))
    
    # Convert to standard format
    standardized = []
    for i, item in enumerate(sampled):
        standardized.append({
            "item_id": f"math_{i}",
            "domain": "math",
            "question": item["problem"],
            "ground_truth": item["solution"]
        })
    return standardized

def load_code(mode):
    print("Loading HumanEval+ dataset...")
    # HumanEval+ 
    ds = load_dataset('evalplus/humanevalplus', split='test')
    
    num_samples = 10 if mode == "pilot" else 150
    sampled = ds.shuffle(seed=42).select(range(num_samples))
    
    standardized = []
    for i, item in enumerate(sampled):
        standardized.append({
            "item_id": f"code_{item['task_id'].replace('/', '_')}",
            "domain": "code",
            "question": item["prompt"],
            "entry_point": item["entry_point"],
            "test": item["test"],
            "ground_truth": item["canonical_solution"]
        })
    return standardized

def load_science(mode):
    print("Loading GPQA-Diamond dataset...")
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError(
            "HF_TOKEN is missing. GPQA-Diamond is gated, so add HF_TOKEN to your .env file before loading science data."
        )
    ds = load_dataset("Idavidrein/gpqa", "gpqa_diamond", split="train", token=token)
    num_samples = 10 if mode == "pilot" else 150
    sampled = ds.shuffle(seed=42)
    standardized = []
    skipped = []
    for item in sampled:
        if len(standardized) >= num_samples:
            break
        item_index = len(standardized)
        random.seed(42 + item_index)
        options = [
            str(item["Correct Answer"]).strip(),
            str(item["Incorrect Answer 1"]).strip(),
            str(item["Incorrect Answer 2"]).strip(),
            str(item["Incorrect Answer 3"]).strip(),
        ]
        random.shuffle(options)
        issues = validate_science_options(options)
        if issues:
            skipped.append({
                "question_preview": str(item["Question"])[:120],
                "issues": issues,
            })
            continue
        option_map = build_option_map(options)
        question_text = render_science_question(str(item["Question"]), options)
        correct_letter = next(
            label for label, option_text in option_map.items()
            if option_text == str(item["Correct Answer"]).strip()
        )
        standardized.append({
            "item_id": f"science_{item_index}",
            "domain": "science",
            "question_stem": str(item["Question"]).strip(),
            "question": question_text,
            "ground_truth": correct_letter,
            "correct_answer_text": str(item["Correct Answer"]).strip(),
            "option_map": option_map,
            "options": [option_map[chr(65 + idx)] for idx in range(4)],
            "source_dataset": "Idavidrein/gpqa:gpqa_diamond",
        })
    if len(standardized) < num_samples:
        raise RuntimeError(
            f"Could only prepare {len(standardized)} valid science items out of requested {num_samples}. "
            f"Skipped {len(skipped)} malformed items."
        )
    if skipped:
        print(f"Skipped {len(skipped)} malformed GPQA items while building the science split.")
        for skipped_item in skipped[:5]:
            print(f"  - {skipped_item['issues']} | {skipped_item['question_preview']}...")
    return standardized

def save_data(data, domain, mode, overwrite=False):
    suffix = "_pilot.jsonl" if mode == "pilot" else ".jsonl"
    out_path = os.path.join(RAW_DATA_DIR, f"{domain}{suffix}")
    
    if overwrite:
        with open(out_path, "w", encoding="utf-8") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")
        print(f"Overwrote {out_path} with {len(data)} items.")
        return

    # Check existing items for resume support and withheld placeholders
    existing_items = {}
    has_withheld = False
    if os.path.exists(out_path):
        with open(out_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    loaded = json.loads(line)
                    existing_items[loaded["item_id"]] = loaded
                    if "[WITHHELD" in str(loaded.get("question", "")):
                        has_withheld = True
                except Exception:
                    pass
    
    # If the file contains withheld placeholders (e.g. from the public sanitized release),
    # replace them with the newly loaded real questions.
    if has_withheld:
        print(f"Detected [WITHHELD] placeholders in {out_path}. Replacing with downloaded data...")
        data_by_id = {item["item_id"]: item for item in data}
        merged_items = []
        for item_id, existing in existing_items.items():
            if item_id in data_by_id:
                merged_items.append(data_by_id[item_id])
            else:
                merged_items.append(existing)
        for item in data:
            if item["item_id"] not in existing_items:
                merged_items.append(item)
                
        with open(out_path, "w", encoding="utf-8") as f:
            for item in merged_items:
                f.write(json.dumps(item) + "\n")
        print(f"Successfully updated {len(merged_items)} items in {out_path}.")
        return

    new_items = [item for item in data if item["item_id"] not in existing_items]
    
    if not new_items:
        print(f"Already have {len(existing_items)} items for {domain} in {out_path}. Nothing to add.")
        return
    
    with open(out_path, "a", encoding="utf-8") as f:
        for item in new_items:
            f.write(json.dumps(item) + "\n")
    print(f"Added {len(new_items)} new items to {out_path} (total: {len(existing_items) + len(new_items)})")

def restore_unredacted_science_outputs(mode):
    """Replace the released (redacted) science candidates/traces with the
    pre-redaction versions kept in the project's git history.

    The raw dataset restore above only rebuilds data/raw/science*.jsonl. The released
    data/generated and data/verified science files were also redacted (option text in
    candidates and verifier reasoning), and no local computation can rebuild them.
    A reader holding the gated dataset is entitled to the full local data, so after the
    raw restore we swap in the newest history version that predates the redaction.
    These restored files stay on this machine; committing them back to the public
    release would re-publish the gated option text.
    """
    suffix = "_pilot.jsonl" if mode == "pilot" else ".jsonl"
    restored = []
    for rel in (os.path.join("data", "generated", f"science{suffix}"),
                os.path.join("data", "verified", f"science{suffix}")):
        if not os.path.exists(rel):
            continue  # pilot outputs are not part of the release
        with open(rel, encoding="utf-8") as f:
            if OPTION_PLACEHOLDER not in f.read():
                continue  # already unredacted
        git_path = rel.replace(os.sep, "/")
        try:
            shas = subprocess.run(
                ["git", "log", "--format=%H", "--", git_path],
                capture_output=True, text=True, check=True).stdout.split()
        except (OSError, subprocess.CalledProcessError):
            print(f"  [5/5] could not read git history for {rel}; it stays redacted.")
            continue
        for sha in shas:
            try:
                content = subprocess.run(
                    ["git", "show", f"{sha}:{git_path}"],
                    capture_output=True, text=True, check=True).stdout
            except subprocess.CalledProcessError:
                continue
            if content and OPTION_PLACEHOLDER not in content:
                with open(rel, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [5/5] restored unredacted {rel} from history ({sha[:7]})")
                restored.append(rel)
                break
        else:
            print(f"  [5/5] no pre-redaction version of {rel} found in history.")
    if restored:
        print("  NOTE: restored files contain gated GPQA option text. They are local to")
        print("        this machine; do not commit them back to the public release.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, choices=["pilot", "actual"], default="pilot")
    parser.add_argument("--domain", type=str, choices=["all", "math", "code", "science"], default="all")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing raw data and save fresh")
    args = parser.parse_args()

    domains = ["math", "code", "science"] if args.domain == "all" else [args.domain]
    
    for domain in domains:
        if domain == "math":
            data = load_math(args.mode)
        elif domain == "code":
            data = load_code(args.mode)
        elif domain == "science":
            data = load_science(args.mode)
        save_data(data, domain, args.mode, overwrite=args.overwrite)
        if domain == "science":
            restore_unredacted_science_outputs(args.mode)

    print("Data loading complete.")
