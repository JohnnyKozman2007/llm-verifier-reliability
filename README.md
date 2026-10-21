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

GPQA-Diamond question text is withheld per the dataset's terms; `python src/data_loader.py`
(with `HF_TOKEN`) restores it.

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

Note: code-candidate correctness is re-graded by executing candidates against the tests with a
5-second timeout, so a few slow HumanEval items can flip on a slower machine and shift headline
numbers by ~0.1 pp. The CSVs committed under `reports/` are the reference results.

## Citation
Citation to be added.
