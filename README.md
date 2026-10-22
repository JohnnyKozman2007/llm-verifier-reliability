# LLM Verifier Reliability

Code, prompts, and verification traces for **"Neither Blinding Nor a Jury, Neither
Capability Nor Strategy: What Brings a Verifier to Reliability"**
(TAE workshop, NeurIPS 2026).

64,800 verification calls: 4 models x 3 authorship frames x 3 strategies x 3 domains
(HumanEval+, MATH, GPQA-Diamond), 150 items per domain.

## Layout
- `src/` pipeline (generate, verify, execution grounding, differential fuzzing) and `src/probes/`
- `data/` benchmark items, candidates, verification traces, fuzzing results
- `reports/` summary CSVs and probe reports; `plots/` figures
- `prompts/` rewrite prompts used in the style-transfer probe
- `paper/` workshop paper sources (numbers aligned with the corrected MATH grader)

GPQA-Diamond item text is withheld in every released artifact. Science traces carry item
ids, answer letters, extracted-parse metadata and verdicts, but no stems, no option strings
and no candidate or verifier prose; code and mathematics traces are released in full. The
curators ask that examples not be revealed in plain text, so nothing here reproduces a GPQA
item. `python src/data_loader.py` (with `HF_TOKEN`) restores the items locally.

## Reproduce
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                              # add DEEPINFRA_API_KEY (and HF_TOKEN for GPQA)
python preflight_check.py
python src/stratified_estimator.py                # headline +13.1 pp self-preference gap
python run.py --mode actual --domain all          # full pipeline (needs API access)
python src/report.py --mode actual --domains all
python src/probes/analysis_ensemble.py            # other probes live in src/probes/
```
Pilot-run files are not included; `--mode pilot` regenerates them.

### Two reproduction paths

**From the release, no credentials.** Everything in `reports/` regenerates from the
committed traces:
```bash
python src/report.py --mode actual --domains all
```
Science grading reads the option letter recorded at verification time instead of re-parsing
candidate text, so the released records reproduce the published numbers. If the letters are
missing, report generation aborts with an error rather than silently grading redacted rows
as wrong.

**From scratch, with credentials.** `HF_TOKEN` for the gated GPQA-Diamond download, plus a
serving API key:
```bash
python src/data_loader.py --mode actual --domain science   # replaces [WITHHELD] rows
python run.py --mode actual --domain science
```

### Keeping the release clean

```bash
python src/redact_release.py          # redact data/ and reports/ in place (idempotent)
python src/redact_release.py --check  # exit 1 if any GPQA item text is present
```
Run the redactor before every commit that touches `data/` or `reports/`. The same check runs
as `tests/test_release_redaction.py`.

Note: code-candidate correctness is re-graded by executing candidates against the tests with a
5-second timeout, so a few slow HumanEval items can flip on a slower machine and shift headline
numbers by ~0.1 pp. The CSVs committed under `reports/` are the reference results.

## Citation
Citation to be added.
