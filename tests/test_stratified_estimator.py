"""
The self-preference estimator must compute every number it reports from the traces.

An earlier version printed a literal self FPR, a hard-coded standard error and a fixed
per-model table, and dropped strata chosen by the sign of their own effect.
"""
import os
import shutil
import sys
import unittest
import uuid

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from stratified_estimator import run_stratified_estimator  # noqa: E402


def _grid(self_verdict, other_verdicts, items):
    """Wrong qwen candidates judged by qwen itself and by other verifiers, in all 9 cells."""
    rows = []
    for item in items:
        for frame in ("self", "other", "neutral"):
            for strategy in ("direct", "cot", "rubric"):
                for verifier, verdict in [("qwen", self_verdict)] + list(other_verdicts.items()):
                    rows.append({
                        "domain": "math", "item_id": item, "generator": "qwen", "verifier": verifier,
                        "frame": frame, "strategy": strategy, "candidate_is_correct": False,
                        "strict_json_parse_fail": 0, "parsed_verdict": verdict,
                    })
    return rows


def _leniency_grid():
    """No self-preference at all: mistral approves every error, qwen and llama none.
    Mistral wrote three of the five errors, so its errors dominate the strata."""
    rows = []
    for generator, items in (("mistral", ("m1", "m2", "m3")), ("qwen", ("q1",)), ("llama", ("l1",))):
        for item in items:
            for frame in ("self", "other", "neutral"):
                for strategy in ("direct", "cot", "rubric"):
                    for verifier in ("mistral", "qwen", "llama"):
                        rows.append({
                            "domain": "math", "item_id": item, "generator": generator, "verifier": verifier,
                            "frame": frame, "strategy": strategy, "candidate_is_correct": False,
                            "strict_json_parse_fail": 0, "parsed_verdict": verifier == "mistral",
                        })
    return rows


class StratifiedEstimator(unittest.TestCase):
    def setUp(self):
        # Created explicitly rather than with mkdtemp: the sandbox denies creating
        # subdirectories inside a mkdtemp directory.
        self.tmp = os.path.join(ROOT, "tests", f".tmp_estimator_{uuid.uuid4().hex}")
        os.makedirs(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def _run(self, rows):
        path = os.path.join(self.tmp, "granular.csv")
        pd.DataFrame(rows).to_csv(path, index=False)
        return run_stratified_estimator(path, self.tmp)

    def test_numbers_come_from_the_data(self):
        out = self._run(_grid(True, {"deepseek": True, "llama": False}, ("i1", "i2", "i3")))
        self.assertEqual(out["strata"], 27)
        self.assertEqual(out["distinct_errors"], 3)
        self.assertAlmostEqual(out["self_fpr"], 100.0)
        self.assertAlmostEqual(out["other_fpr"], 50.0)
        self.assertAlmostEqual(out["gap"], 50.0)
        self.assertAlmostEqual(out["se"], 0.0)

    def test_strata_against_the_effect_are_kept(self):
        # On i3 the author approves less often than the others; those strata must stay in.
        rows = (_grid(True, {"deepseek": False, "llama": False}, ("i1", "i2"))
                + _grid(False, {"deepseek": True, "llama": True}, ("i3",)))
        out = self._run(rows)
        self.assertEqual(out["strata"], 27)
        self.assertAlmostEqual(out["gap"], (2 * 100 - 100) / 3)
        self.assertGreater(out["se"], 0.0)

    def test_judge_fixed_estimate_removes_a_lenient_judge_artifact(self):
        out = self._run(_leniency_grid())
        # Holding only the error fixed, mistral's leniency on its own errors reads as self-preference.
        self.assertAlmostEqual(out["gap"], 40.0)
        self.assertAlmostEqual(out["judge_fixed_gap"], 0.0, places=6)
        # Without mistral, qwen and llama treat every error alike: no gap either way.
        self.assertAlmostEqual(out["gap_no_mistral"], 0.0)
        self.assertAlmostEqual(out["judge_fixed_gap_no_mistral"], 0.0, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
