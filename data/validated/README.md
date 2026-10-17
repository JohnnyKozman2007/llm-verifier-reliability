# Code-domain adjudication traces

`code_overrides.jsonl` — verifier rejected a candidate that passed its test suite, with a
differential-fuzzing verdict for each case.
`code_missed_failures.jsonl` — verifier approved a candidate that failed its test suite.

## These files are a superset of the released run

`validate_overrides.py` appends to them rather than rebuilding, so both accumulated rows
from an earlier verification pass:

| File | Rows in file | Rows in the released run |
|---|---:|---:|
| `code_overrides.jsonl` | 1,856 | **1,458** |
| `code_missed_failures.jsonl` | 1,580 | **1,158** |

The extra rows describe verifications that are not in `data/verified/code.jsonl`. They are
kept for provenance, but **every figure reported in `reports/` and in the paper is computed
over the subset that is present there** — so counting the raw file directly will not match.
Most visibly, the raw file gives 9.0 % `BUG_CONFIRMED` where the reported figure is 7.3 %.

## Reproducing the reported figures

Select the rows whose `(item_id, generator_model, verifier_model, frame, strategy)` key
appears in `data/verified/code.jsonl` with `overrode_passing_tests` true:

```python
import json, collections

KEY = ("item_id", "generator_model", "verifier_model", "frame", "strategy")
traces = [json.loads(l) for l in open("data/verified/code.jsonl", encoding="utf-8")]
released = {tuple(t[k] for k in KEY) for t in traces if t["overrode_passing_tests"]}

rows = [json.loads(l) for l in open("data/validated/code_overrides.jsonl", encoding="utf-8")]
rows = [r for r in rows if tuple(r[k] for k in KEY) in released]

counts = collections.Counter(r["fuzz_verdict"] for r in rows)
print(len(rows), {v: f"{100 * n / len(rows):.1f}%" for v, n in counts.most_common()})
```

which prints

```
1458 {'NO_DISCREPANCY': '77.2%', 'SKIPPED_PIPELINE_FAIL': '11.5%', 'BUG_CONFIRMED': '7.3%', 'ERROR': '3.2%', 'REFERENCE_BUG': '0.8%'}
```

matching Appendix A. The same filter applied to `code_missed_failures.jsonl` — swapping the
predicate for `execution_ran_successfully` false and `parsed_verdict` true — leaves 1,158 rows.
The four `REFERENCE_BUG` items are `code_HumanEval_17`, `_59`, `_126` and `_134`.
