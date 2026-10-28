# LLM Verifier Reliability

Code, prompts, and verification traces for **"Neither Blinding Nor a Jury, Neither
Capability Nor Strategy: What Brings a Verifier to Reliability"**
accepted at two NeurIPS 2026 workshops:
- Workshop on Who Verifies the Agents? Toward Reliable Agent Development, NeurIPS 2026
- Workshop on TAE (Trust-AI-Eval): Can We Trust AI Evaluation?, NeurIPS 2026

The two camera-ready builds share one paper body and differ only in the footer.

64,800 verification calls: 4 generators x 4 verifiers x 3 authorship frames x 3 strategies,
over 3 domains (HumanEval+, MATH, GPQA-Diamond) of 150 items each.

## Layout
- `src/` pipeline (generate, verify, execution grounding, differential fuzzing) and `src/probes/`
- `data/` benchmark items, candidates, verification traces, fuzzing results
- `reports/` summary CSVs and probe reports; `plots/` figures
- `prompts/` rewrite prompts used in the style-transfer probe
- `paper/` workshop paper sources (numbers aligned with the corrected MATH grader): `paper.tex` is
  the shared body; `verify-agents/main.tex` and `tae/main.tex` build each workshop's camera-ready; `arxiv/` contains the self-contained arXiv preprint build

GPQA-Diamond item text is withheld in every released artifact. Science traces carry item
ids, answer letters, extracted-parse metadata and verdicts, but no stems, no option strings
and no candidate or verifier prose; code and mathematics traces are released in full. The
curators ask that examples not be revealed in plain text, so nothing here reproduces a GPQA
item. `python src/data_loader.py` (with `HF_TOKEN`) restores the items locally.

## Licence

Code (`src/`, `tests/`, `prompts/`, `run.py`) is MIT. The derived artifacts (`data/`,
`reports/`, `plots/`) are CC BY 4.0. Third-party benchmarks keep their own terms:
HumanEval+/EvalPlus (Apache-2.0, built on OpenAI's HumanEval under MIT), MATH (MIT),
GPQA-Diamond (CC BY 4.0). GPQA-Diamond is credited in the paper as
*GPQA: A Graduate-Level Google-Proof Q&A Benchmark*, Rein et al. (2024),
https://github.com/idavidrein/gpqa, with our changes stated: a 150-item subsample and
per-item option re-ordering. See `LICENSE`, and `THIRD_PARTY_NOTICES.md` for the upstream
licence notices that travel with the copied MATH and HumanEval+ items.

The traces also contain outputs of the models that were run, each under its own terms:
Qwen2.5-72B-Instruct (Qwen License), DeepSeek-V3 (DeepSeek Model License),
Llama-3.3-70B-Instruct (Llama 3.3 Community License), Mistral-Nemo-Instruct-2407 and
Mixtral-8x7B-Instruct-v0.1 (Apache-2.0), Gemma-2-27B-it (Gemma Terms of Use), and
WizardLM-2-8x22B (Apache-2.0 per its release model card; the official page is no longer
public). They are released for research on verifier reliability; no model was trained on
them.

## Reproduce
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                              # add DEEPINFRA_API_KEY (and HF_TOKEN for GPQA)
python preflight_check.py
python src/stratified_estimator.py                # self-preference: +11.1 pp with error and judge fixed
python run.py --mode actual --domain all          # full pipeline (needs API access)
python src/report.py --mode actual --domains all
python src/probes/analysis_ensemble.py            # other probes live in src/probes/
```
Pilot-run files are not included; `--mode pilot` regenerates them.

### Two reproduction paths

**From the release, no credentials.** The paper's tables and figures regenerate from the
committed traces:
```bash
python src/report.py --mode actual --domains all              # main-grid tables and plots
python src/stratified_estimator.py                            # self-preference gap
python src/probes/analysis_detectability.py                   # detectability (prints)
python src/probes/analysis_oversight.py                       # oversight (prints)
python src/probes/analysis_ensemble.py                        # ensembles, agreement, joint failure
python src/probes/plot_detectability.py
python src/probes/plot_ensemble.py
python src/probes/plot_oversight.py
python src/probes/generate_self_preference_report.py
python src/probes/generate_style_transfer_report.py
python src/probes/analysis_self_recognition.py --domain science
python src/probes/analysis_self_recognition.py --domain math
python src/probes/analysis_self_recognition.py --domain code
python src/probes/plot_self_recognition.py
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
python src/redact_release.py --check  # exit 1 if any GPQA item text or local path is present
```
Run the redactor before every commit that touches `data/` or `reports/`. The same check runs
as `tests/test_release_redaction.py`.

Note: code-candidate correctness is read from the committed labels in
`reports/probes/Do-stronger-models-make-mistakes-that-are-harder-to-catch/graded_code.json`
rather than re-run. Re-executing candidates under the 5-second timeout is not reproducible
across machines: a few slow HumanEval candidates pass on one machine and time out on another.
Delete that file only if you mean to re-grade code from scratch.

## Citation
```bibtex
@misc{kozman2026neither,
  title        = {Neither Blinding Nor a Jury, Neither Capability Nor Strategy:
                  What Brings a Verifier to Reliability},
  author       = {Kozman, Johnny and Parajuli, Tilak and Waddepalli, Arushi},
  year         = {2026},
  howpublished = {NeurIPS 2026 Workshops: Who Verifies the Agents? Toward Reliable Agent
                  Development; TAE (Trust-AI-Eval): Can We Trust AI Evaluation?},
  url          = {https://github.com/JohnnyKozman2007/llm-verifier-reliability}
}
```
The same metadata is in `CITATION.cff`.
