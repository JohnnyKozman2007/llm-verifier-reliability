# Dynamic Executive Summary

**Total Verifications Processed:** 64800
**Pipeline Failures Handled:** 244 (These defaulted to basic test suite results rather than dropping rows)

## Highest Accuracy by Domain
![Accuracy Plot](../../../plots/actual/all/actual_all_accuracy_by_domain.png)

- **Code**: mistral (Frame: self, Strategy: direct) achieved **97.3%** accuracy (**97.3% Adjusted**).
- **Math**: deepseek (Frame: neutral, Strategy: rubric) achieved **80.8%** accuracy (**80.8% Adjusted**).
- **Science**: deepseek (Frame: other, Strategy: cot) achieved **65.8%** accuracy (**65.8% Adjusted**).

## Model Preferences by Domain (Best Configurations)
### Code
- **deepseek**: Prefers **other** frame & **direct** strategy (**91.7%**)
- **llama**: Prefers **other** frame & **cot** strategy (**92.2%**)
- **mistral**: Prefers **self** frame & **direct** strategy (**97.3%**)
- **qwen**: Prefers **neutral** frame & **direct** strategy (**97.0%**)
### Math
- **deepseek**: Prefers **neutral** frame & **rubric** strategy (**80.8%**)
- **llama**: Prefers **self** frame & **cot** strategy (**78.7%**)
- **mistral**: Prefers **other** frame & **rubric** strategy (**71.2%**)
- **qwen**: Prefers **other** frame & **direct** strategy (**79.7%**)
### Science
- **deepseek**: Prefers **other** frame & **cot** strategy (**65.8%**)
- **llama**: Prefers **self** frame & **cot** strategy (**60.8%**)
- **mistral**: Prefers **self** frame & **rubric** strategy (**53.0%**)
- **qwen**: Prefers **neutral** frame & **rubric** strategy (**59.2%**)

## Strategy Performance per Model (Raw Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 77.9% | 77.9% | 77.7% |
| **llama** | 76.4% | 73.5% | 75.6% |
| **mistral** | 64.2% | 71.4% | 61.9% |
| **qwen** | 75.5% | 77.4% | 75.9% |

## Strategy Performance per Model (Adjusted Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 78.0% | 77.9% | 77.7% |
| **llama** | 76.4% | 73.6% | 75.6% |
| **mistral** | 64.4% | 71.4% | 62.3% |
| **qwen** | 75.5% | 77.3% | 75.9% |

## 1. Comprehensive Accuracy Breakdown (Raw)
### Overall Average Across Everything
- **Overall**: 73.8%
### By Domain
- **Code**: 87.3%
- **Math**: 76.8%
- **Science**: 57.2%
### By Strategy
- **cot**: 73.5%
- **direct**: 75.0%
- **rubric**: 72.8%
### By Ownership Frame
- **neutral**: 73.3%
- **other**: 73.8%
- **self**: 74.2%
### By Model
- **deepseek**: 77.8%
- **llama**: 75.2%
- **mistral**: 65.8%
- **qwen**: 76.2%
### Top 3 Best Ownership + Strategy Combos
- **self + direct**: 75.3%
- **other + direct**: 75.1%
- **neutral + direct**: 74.7%

## 1b. Comprehensive Accuracy Breakdown (Adjusted)
### Overall Average Across Everything
- **Overall**: 73.8%
### By Domain
- **Code**: 87.5%
- **Math**: 76.8%
- **Science**: 57.2%
### By Strategy
- **cot**: 73.6%
- **direct**: 75.1%
- **rubric**: 72.9%
### By Ownership Frame
- **neutral**: 73.4%
- **other**: 73.9%
- **self**: 74.3%
### By Model
- **deepseek**: 77.9%
- **llama**: 75.2%
- **mistral**: 66.1%
- **qwen**: 76.2%
### Top 3 Best Ownership + Strategy Combos
- **self + direct**: 75.4%
- **other + direct**: 75.1%
- **neutral + direct**: 74.7%

## 2. Formatting Failure Rates (NaN / Instructions Missed)
### Overall Average Across Everything
- **Overall**: 0.0%
### By Domain
- **Code**: 0.0%
- **Math**: 0.0%
- **Science**: 0.0%
### By Strategy
- **cot**: 0.0%
- **direct**: 0.0%
- **rubric**: 0.0%
### By Ownership Frame
- **neutral**: 0.0%
- **other**: 0.0%
- **self**: 0.0%
### By Model
- **deepseek**: 0.0%
- **llama**: 0.0%
- **mistral**: 0.0%
- **qwen**: 0.0%
### Top 3 Best Ownership + Strategy Combos
- **neutral + cot**: 0.0%
- **neutral + direct**: 0.0%
- **neutral + rubric**: 0.0%

## 3. Verbosity Analysis (Average Characters)
### Overall Average Across Everything
- **Overall**: 194.5
### By Domain
- **Code**: 192.9
- **Math**: 180.0
- **Science**: 210.6
### By Strategy
- **cot**: 314.2
- **direct**: 0.0
- **rubric**: 269.3
### By Ownership Frame
- **neutral**: 194.1
- **other**: 194.5
- **self**: 194.9
### By Model
- **deepseek**: 189.3
- **llama**: 239.4
- **mistral**: 173.3
- **qwen**: 176.0
### Top 3 Best Ownership + Strategy Combos
- **other + cot**: 314.7
- **self + cot**: 314.6
- **neutral + cot**: 313.2

## 5. Verifier Behavior Rates
### Overall Averages
- **Overall** -> Caught: 50.7% | Passed: 49.3% | Introduced: 11.4% | Confirmed: 88.6%
### By Domain
- **code** -> Caught: 81.4% | Passed: 18.6% | Introduced: 10.0% | Confirmed: 90.0%
- **math** -> Caught: 36.5% | Passed: 63.5% | Introduced: 4.8% | Confirmed: 95.2%
- **science** -> Caught: 41.9% | Passed: 58.1% | Introduced: 23.6% | Confirmed: 76.4%
### By Strategy
- **cot** -> Caught: 51.1% | Passed: 48.9% | Introduced: 12.0% | Confirmed: 88.0%
- **direct** -> Caught: 48.5% | Passed: 51.5% | Introduced: 7.8% | Confirmed: 92.2%
- **rubric** -> Caught: 52.6% | Passed: 47.4% | Introduced: 14.2% | Confirmed: 85.8%
### By Ownership Frame
- **neutral** -> Caught: 49.5% | Passed: 50.5% | Introduced: 11.4% | Confirmed: 88.6%
- **other** -> Caught: 51.0% | Passed: 49.0% | Introduced: 11.4% | Confirmed: 88.6%
- **self** -> Caught: 51.6% | Passed: 48.4% | Introduced: 11.2% | Confirmed: 88.8%
### By Model
- **deepseek** -> Caught: 64.3% | Passed: 35.7% | Introduced: 13.5% | Confirmed: 86.5%
- **llama** -> Caught: 49.8% | Passed: 50.2% | Introduced: 8.4% | Confirmed: 91.6%
- **mistral** -> Caught: 36.5% | Passed: 63.5% | Introduced: 15.2% | Confirmed: 84.8%
- **qwen** -> Caught: 52.3% | Passed: 47.7% | Introduced: 8.3% | Confirmed: 91.7%

## 6. Statistical Bias (Self vs Other)
### Top 3 Highest Self-Preservation Biases (FPR Gap)
*These models were most likely to falsely approve their own mistakes.*
![FPR Bias Plot](../../../plots/actual/all/actual_all_fpr_self_bias.png)

- **mistral** (math, rubric): **+4.8%** bias
- **mistral** (code, rubric): **+3.3%** bias
- **deepseek** (math, rubric): **+3.2%** bias

### Top 3 Highest Self-Doubt Biases (FNR Gap)
*These models were most likely to falsely reject their own correct answers.*
![FNR Bias Plot](../../../plots/actual/all/actual_all_fnr_self_bias.png)

- **llama** (science, rubric): **+4.9%** bias
- **llama** (science, cot): **+4.2%** bias
- **llama** (code, cot): **+2.4%** bias

### Statistical Significance (P-Values for Bias) — Raw numbers, chi-square per (verifier, domain, strategy) cell.
*Small pilot sample sizes (~20/cell) mean most will read as not significant; that's expected at this scale.*
- **mistral** (math, rubric): FPR Bias p=0.2865 | FNR Bias p=0.8794
- **mistral** (code, rubric): FPR Bias p=0.3255 | FNR Bias p=0.5320
- **deepseek** (math, rubric): FPR Bias p=0.5976 | FNR Bias p=0.8257

## 6b. Statistical Bias — Fuzz-Adjusted (Corrected Ground Truth)
*Same analysis as Section 6 but using fuzz-adjusted ground truth for the code domain. Rows where the fuzzer found a `REFERENCE_BUG` (reference was wrong) or `BUG_CONFIRMED` (candidate had a real bug) are reclassified before computing FPR/FNR. For math and science domains the adjusted numbers are identical to raw. Differences between raw and adjusted in code domain reflect the impact of oracle corrections.*

### Top 3 Highest Adjusted Self-Preservation Biases (Adj FPR Gap)
![Adj FPR Bias Plot](../../../plots/actual/all/actual_all_adj_fpr_self_bias.png)

- **mistral** (math, rubric): **+4.8%** adjusted bias
- **mistral** (math, cot): **+3.2%** adjusted bias
- **deepseek** (math, rubric): **+3.2%** adjusted bias

### Top 3 Highest Adjusted Self-Doubt Biases (Adj FNR Gap)
![Adj FNR Bias Plot](../../../plots/actual/all/actual_all_adj_fnr_self_bias.png)

- **llama** (science, rubric): **+4.9%** adjusted bias
- **llama** (science, cot): **+4.2%** adjusted bias
- **llama** (code, cot): **+2.4%** adjusted bias

### Statistical Significance (P-Values for Adjusted Bias)
- **mistral** (math, rubric): Adj FPR Bias p=0.2865 | Adj FNR Bias p=0.8794
- **mistral** (math, cot): Adj FPR Bias p=0.4689 | Adj FNR Bias p=0.4495
- **deepseek** (math, rubric): Adj FPR Bias p=0.5976 | Adj FNR Bias p=0.8257

Full adjusted bias table: `actual_all_adj_bias_metrics.csv`.

## 6c. Oracle & Fuzzing Statistics (Code Domain)
*These rows represent code verifications where the verifier overrode a passing execution result (i.e. test passed but verifier said incorrect). The fuzzer ran differential testing on each and an LLM oracle adjudicated mismatches. This section quantifies how often the verifier was right vs. wrong, and how often the benchmark reference itself was the problem.*

**Total override cases fuzzed:** 1458

### Verdict Breakdown

| Verdict | Count | % of Fuzzed |
|---|---|---|
| `BUG_CONFIRMED` | 107 | 7.3% |
| `REFERENCE_BUG` | 11 | 0.8% |
| `NO_DISCREPANCY` | 1125 | 77.2% |
| `SKIPPED_PIPELINE_FAIL` | 168 | 11.5% |
| `ERROR` | 47 | 3.2% |

### REFERENCE_BUG Deep Dive (11 cases)
*These are items where the HumanEval+ reference solution itself appears to be incorrect. The verifier's override was justified — the candidate was actually more correct than the reference.*

**Affected item IDs:** code_HumanEval_126, code_HumanEval_134, code_HumanEval_17, code_HumanEval_59

**By generator model (which model's candidate was vindicated):**
- deepseek: 5
- qwen: 5
- llama: 1

### Verdicts by Verifier Model

| Verifier | BUG_CONFIRMED | REFERENCE_BUG | NO_DISCREPANCY | SKIPPED_PIPELINE_FAIL | ERROR |
|---|---|---|---|---|---|
| deepseek | 7 | 3 | 106 | 10 | 11 |
| llama | 15 | 0 | 138 | 18 | 5 |
| mistral | 85 | 8 | 838 | 132 | 28 |
| qwen | 0 | 0 | 43 | 8 | 3 |

### Verdicts by Generator Model

| Generator | BUG_CONFIRMED | REFERENCE_BUG | NO_DISCREPANCY | SKIPPED_PIPELINE_FAIL | ERROR |
|---|---|---|---|---|---|
| deepseek | 29 | 5 | 354 | 40 | 10 |
| llama | 42 | 1 | 231 | 50 | 21 |
| mistral | 10 | 0 | 220 | 17 | 3 |
| qwen | 26 | 5 | 320 | 61 | 13 |

### Verifier Override Accuracy
*% of overrides that were JUSTIFIED (BUG_CONFIRMED) vs. UNJUSTIFIED (NO_DISCREPANCY or REFERENCE_BUG)*

| Verifier | Total Overrides | Justified (%) | Unjustified (%) | Inconclusive (%) |
|---|---|---|---|---|
| deepseek | 137 | 5.1% | 79.6% | 15.3% |
| llama | 176 | 8.5% | 78.4% | 13.1% |
| mistral | 1091 | 7.8% | 77.5% | 14.7% |
| qwen | 54 | 0.0% | 79.6% | 20.4% |


## 7. Domain-Specific Validity Checks
*These checks are diagnostic safeguards around domain-specific grading. They support the shared metrics above; they do not replace the common accuracy/FPR/FNR analysis.*

Full table: `actual_all_domain_validity_checks.csv`.

### Code: Execution Grounding
*Instances where the code passed the test suite, but the verifier LLM overrode that execution signal and marked it INCORRECT.*
- **Total Overrides**: 1458 out of 15012 passing submissions.

#### By Verifier Model
- **deepseek**: 137
- **llama**: 176
- **mistral**: 1091
- **qwen**: 54

### Science: Option Extraction Audit
*Science grading uses the shared correctness metrics above, with an additional parser audit because GPQA answers must map cleanly to one of A-D.*
- **Candidate Parse Rate**: 99.8% of science verification rows had a detected A-D answer.
- **Ambiguous Candidate Rate**: 0.2% of science verification rows were marked ambiguous by the parser.
- **Best Science Generator**: deepseek with 51.3% generation accuracy.
- **Best Science Verifier Cell**: deepseek / other / cot at 65.8% accuracy.
- **Highest Science False-Approval Cell**: mistral / neutral / direct with 92.5% FPR.
Full science audit files: `actual_all_science_generation_audit.csv`, `actual_all_science_generator_summary.csv`, `actual_all_science_verifier_diagnostics.csv`.

### Math: Answer Matching
- Math candidates are graded by final-answer extraction, then exact-rational and canonical-form matching: formatting-equivalent answers (plain vs. LaTeX fractions, reduced or not, decimal equivalents, sqrt/pi notation) are accepted. Algebraically equivalent but structurally different rewrites (e.g. factored vs. expanded forms) remain a limitation to mention in the paper.
- **Math Verification Rows**: 21600

## 8. Belief vs. Reality (Told Frame vs. Actual Authorship)
*Answers Primary Question 1: does TELLING a verifier 'you wrote this' change its accuracy, independent of whether that's true? Rows below cross the told frame against ground-truth authorship (actual_source).*

| Verifier | Told Frame | Actually Self-Authored? | Accuracy | FPR |
|---|---|---|---|---|
| deepseek | other | No | 78.6% | 29.9% |
| deepseek | other | Yes | 77.0% | 54.1% |
| deepseek | self | No | 78.3% | 30.7% |
| deepseek | self | Yes | 76.4% | 55.5% |
| llama | other | No | 74.4% | 50.5% |
| llama | other | Yes | 76.5% | 56.2% |
| llama | self | No | 75.3% | 46.1% |
| llama | self | Yes | 78.7% | 49.0% |
| mistral | other | No | 67.9% | 63.5% |
| mistral | other | Yes | 59.5% | 60.1% |
| mistral | self | No | 69.0% | 64.3% |
| mistral | self | Yes | 59.5% | 62.5% |
| qwen | other | No | 77.5% | 42.2% |
| qwen | other | Yes | 73.0% | 63.5% |
| qwen | self | No | 77.5% | 42.5% |
| qwen | self | Yes | 72.7% | 63.7% |

Read this as 2x2 per verifier: (told self / actually self) vs (told self / actually other) vs (told other / actually self) vs (told other / actually other). A gap between the first two rows (same actual authorship, different label) isolates the pure *belief* effect. A gap between rows 1 and 3 (same label, different truth) isolates the pure *reality* effect. Full data: `actual_all_belief_vs_reality.csv`.

## 9. Confusion Matrices (Visuals & Raw Data)
### deepseek
**True Positives:** 8520 | **False Positives:** 2267 | **True Negatives:** 4087 | **False Negatives:** 1326

![Confusion Matrix deepseek](../../../plots/actual/all/actual_all_confusion_matrix_deepseek.png)
### llama
**True Positives:** 9016 | **False Positives:** 3190 | **True Negatives:** 3164 | **False Negatives:** 830

![Confusion Matrix llama](../../../plots/actual/all/actual_all_confusion_matrix_llama.png)
### mistral
**True Positives:** 8347 | **False Positives:** 4037 | **True Negatives:** 2317 | **False Negatives:** 1499

![Confusion Matrix mistral](../../../plots/actual/all/actual_all_confusion_matrix_mistral.png)
### qwen
**True Positives:** 9029 | **False Positives:** 3033 | **True Negatives:** 3321 | **False Negatives:** 817

![Confusion Matrix qwen](../../../plots/actual/all/actual_all_confusion_matrix_qwen.png)
