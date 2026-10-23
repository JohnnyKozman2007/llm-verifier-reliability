"""Guards the release against GPQA-Diamond item text.

The pipeline needs the question text; the release must not contain it. These tests fail if
a regenerated trace set is committed without running `python src/redact_release.py`, or if
the redactor itself regresses.
"""
import json
import os
import shutil
import sys
import uuid
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

import redact_release
from science_utils import SCIENCE_WITHHELD_PLACEHOLDER, is_withheld


class TestReleaseIsRedacted(unittest.TestCase):
    def test_committed_release_has_no_item_text(self):
        problems = redact_release.check(os.path.join(ROOT, "data"), os.path.join(ROOT, "reports"))
        self.assertEqual(problems, [], f"released artifacts still carry GPQA text or local paths: {problems[:5]}")


class TestRedactor(unittest.TestCase):
    def setUp(self):
        # Created explicitly rather than with mkdtemp: the sandbox denies creating
        # subdirectories inside a mkdtemp directory.
        self.tmp = os.path.join(ROOT, "tests", f".tmp_release_{uuid.uuid4().hex}")
        for kind in ("raw", "generated", "verified"):
            os.makedirs(os.path.join(self.tmp, kind), exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def _write(self, kind, rows):
        path = os.path.join(self.tmp, kind, "science.jsonl")
        with open(path, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row) + "\n")
        return path

    def _read(self, kind):
        path = os.path.join(self.tmp, kind, "science.jsonl")
        with open(path, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]

    def test_raw_and_generated_lose_options_and_question(self):
        item = {
            "item_id": "science_0",
            "domain": "science",
            "question_stem": "a real stem",
            "question": "a real stem\nOptions:\nA. x",
            "ground_truth": "D",
            "correct_answer_text": "x",
            "option_map": {"A": "x"},
            "options": ["x"],
        }
        self._write("raw", [item])
        self._write("generated", [dict(item, candidates={"qwen": "model prose quoting x"})])
        redact_release.redact_raw(os.path.join(self.tmp, "raw", "science.jsonl"))
        redact_release.redact_generated(os.path.join(self.tmp, "generated", "science.jsonl"))

        raw = self._read("raw")[0]
        self.assertNotIn("options", raw)
        self.assertNotIn("option_map", raw)
        self.assertNotIn("correct_answer_text", raw)
        self.assertTrue(is_withheld(raw["question"]))
        self.assertEqual(raw["ground_truth"], "D", "answer letter must survive: it is needed to grade")

        gen = self._read("generated")[0]
        self.assertTrue(is_withheld(gen["candidates"]["qwen"]))

    def test_verified_keeps_letters_and_backfills_verbosity(self):
        row = {
            "item_id": "science_0",
            "generator_model": "qwen",
            "verifier_model": "llama",
            "frame": "self",
            "strategy": "direct",
            "parsed_verdict": True,
            "raw_response": '{"is_correct": true}',
            "thinking_or_evaluation": "12345",
            "candidate_answer_letter": "C",
            "candidate_answer_text": "an option string",
        }
        self._write("verified", [row])
        redact_release.redact_verified(os.path.join(self.tmp, "verified", "science.jsonl"))
        out = self._read("verified")[0]
        self.assertEqual(out["candidate_answer_letter"], "C")
        self.assertEqual(out["parsed_verdict"], True)
        self.assertEqual(out["verbosity_chars"], 5)
        for field in ("raw_response", "thinking_or_evaluation", "candidate_answer_text"):
            self.assertTrue(is_withheld(out[field]), field)

    def test_check_flags_an_unredacted_file(self):
        self._write("raw", [{
            "item_id": "science_0",
            "domain": "science",
            "question": "a real stem",
            "options": ["x"],
            "ground_truth": "A",
        }])
        problems = redact_release.check(self.tmp, os.path.join(self.tmp, "reports"))
        self.assertTrue(problems)
        self.assertTrue(any("options" in problem for _, problem in problems))

    def test_local_paths_are_scrubbed_from_validation_traces(self):
        validated = os.path.join(self.tmp, "validated")
        os.makedirs(validated, exist_ok=True)
        path = os.path.join(validated, "code_overrides.jsonl")
        rows = [
            {"item_id": "code_0", "fuzz_note": 'File "C:\\Users\\someone\\AppData\\Local\\Temp\\tmpab12.py", line 3'},
            # truncated mid-path, as some stored notes are
            {"item_id": "code_1", "fuzz_note": 'Harness crashed: rs\\someone\\AppData\\Local\\Temp\\tmpcd34.py", line 3'},
            {"item_id": "code_2", "fuzz_note": "no path here"},
        ]
        with open(path, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row) + "\n")
        reports = os.path.join(self.tmp, "reports")
        self.assertEqual(len(redact_release.check(self.tmp, reports)), 2)

        redact_release.redact_local_paths(validated)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertNotIn("someone", text)
        self.assertIn("tmpab12.py", text, "only the directory is local; the file name stays")
        self.assertIn('{"item_id": "code_2", "fuzz_note": "no path here"}\n', text)
        self.assertEqual(redact_release.check(self.tmp, reports), [])


if __name__ == "__main__":
    unittest.main()
