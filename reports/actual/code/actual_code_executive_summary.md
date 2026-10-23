# Dynamic Executive Summary

**Total Verifications Processed:** 21600
**Pipeline Failures Handled:** 244 (These defaulted to basic test suite results rather than dropping rows)

## Highest Accuracy by Domain
![Accuracy Plot](../../../plots/actual/code/actual_code_accuracy_by_domain.png)

- **Code**: mistral (Frame: self, Strategy: direct) achieved **97.8%** accuracy (**97.8% Adjusted**).

## Model Preferences by Domain (Best Configurations)
### Code
- **deepseek**: Prefers **other** frame & **direct** strategy (**91.8%**)
- **llama**: Prefers **other** frame & **cot** strategy (**92.3%**)
- **mistral**: Prefers **self** frame & **direct** strategy (**97.8%**)
- **qwen**: Prefers **neutral** frame & **direct** strategy (**97.2%**)

## Strategy Performance per Model (Raw Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 89.2% | 91.3% | 89.7% |
| **llama** | 91.8% | 86.8% | 91.1% |
| **mistral** | 71.2% | 97.6% | 63.4% |
| **qwen** | 90.9% | 96.6% | 90.4% |

## Strategy Performance per Model (Adjusted Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 89.3% | 91.4% | 89.8% |
| **llama** | 91.8% | 87.1% | 91.1% |
| **mistral** | 71.9% | 97.8% | 64.8% |
| **qwen** | 90.8% | 96.4% | 90.4% |

## 1. Comprehensive Accuracy Breakdown (Raw)
### Overall Average Across Everything
- **Overall**: 87.5%
### By Domain
- **Code**: 87.5%
### By Strategy
- **cot**: 85.8%
- **direct**: 93.1%
- **rubric**: 83.7%
### By Ownership Frame
- **neutral**: 86.8%
- **other**: 87.4%
- **self**: 88.3%
### By Model
- **deepseek**: 90.1%
- **llama**: 89.9%
- **mistral**: 77.4%
- **qwen**: 92.6%
### Top 3 Best Ownership + Strategy Combos
- **self + direct**: 93.4%
- **other + direct**: 93.0%
- **neutral + direct**: 92.8%

## 1b. Comprehensive Accuracy Breakdown (Adjusted)
### Overall Average Across Everything
- **Overall**: 87.7%
### By Domain
- **Code**: 87.7%
### By Strategy
- **cot**: 86.0%
- **direct**: 93.2%
- **rubric**: 84.0%
### By Ownership Frame
- **neutral**: 87.1%
- **other**: 87.6%
- **self**: 88.5%
### By Model
- **deepseek**: 90.1%
- **llama**: 90.0%
- **mistral**: 78.2%
- **qwen**: 92.6%
### Top 3 Best Ownership + Strategy Combos
- **self + direct**: 93.4%
- **other + direct**: 93.2%
- **neutral + direct**: 92.8%

## 2. Formatting Failure Rates (NaN / Instructions Missed)
### Overall Average Across Everything
- **Overall**: 0.0%
### By Domain
- **Code**: 0.0%
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
- **Overall**: 192.9
### By Domain
- **Code**: 192.9
### By Strategy
- **cot**: 304.3
- **direct**: 0.0
- **rubric**: 274.5
### By Ownership Frame
- **neutral**: 192.4
- **other**: 193.3
- **self**: 193.1
### By Model
- **deepseek**: 187.1
- **llama**: 224.9
- **mistral**: 183.0
- **qwen**: 176.7
### Top 3 Best Ownership + Strategy Combos
- **other + cot**: 305.6
- **self + cot**: 303.9
- **neutral + cot**: 303.3

## 5. Verifier Behavior Rates
### Overall Averages
- **Overall** -> Caught: 82.2% | Passed: 17.8% | Introduced: 10.2% | Confirmed: 89.8%
### By Domain
- **code** -> Caught: 82.2% | Passed: 17.8% | Introduced: 10.2% | Confirmed: 89.8%
### By Strategy
- **cot** -> Caught: 80.4% | Passed: 19.6% | Introduced: 11.9% | Confirmed: 88.1%
- **direct** -> Caught: 85.3% | Passed: 14.7% | Introduced: 3.6% | Confirmed: 96.4%
- **rubric** -> Caught: 80.8% | Passed: 19.2% | Introduced: 15.1% | Confirmed: 84.9%
### By Ownership Frame
- **neutral** -> Caught: 81.0% | Passed: 19.0% | Introduced: 10.8% | Confirmed: 89.2%
- **other** -> Caught: 81.7% | Passed: 18.3% | Introduced: 10.1% | Confirmed: 89.9%
- **self** -> Caught: 83.8% | Passed: 16.2% | Introduced: 9.7% | Confirmed: 90.3%
### By Model
- **deepseek** -> Caught: 76.5% | Passed: 23.5% | Introduced: 4.2% | Confirmed: 95.8%
- **llama** -> Caught: 78.5% | Passed: 21.5% | Introduced: 5.2% | Confirmed: 94.8%
- **mistral** -> Caught: 93.5% | Passed: 6.5% | Introduced: 29.4% | Confirmed: 70.6%
- **qwen** -> Caught: 80.2% | Passed: 19.8% | Introduced: 2.1% | Confirmed: 97.9%

## 6. Statistical Bias (Self vs Other)
### Top 3 Highest Self-Preservation Biases (FPR Gap)
*These models were most likely to falsely approve their own mistakes.*
![FPR Bias Plot](../../../plots/actual/code/actual_code_fpr_self_bias.png)

- **mistral** (code, rubric): **+2.2%** bias
- **qwen** (code, direct): **+0.6%** bias
- **deepseek** (code, rubric): **+0.6%** bias

### Top 3 Highest Self-Doubt Biases (FNR Gap)
*These models were most likely to falsely reject their own correct answers.*
![FNR Bias Plot](../../../plots/actual/code/actual_code_fnr_self_bias.png)

- **llama** (code, cot): **+2.4%** bias
- **llama** (code, rubric): **+1.4%** bias
- **deepseek** (code, direct): **+1.0%** bias

### Statistical Significance (P-Values for Bias) — Raw numbers, chi-square per (verifier, domain, strategy) cell.
*Small pilot sample sizes (~20/cell) mean most will read as not significant; that's expected at this scale.*
- **mistral** (code, rubric): FPR Bias p=0.5413 | FNR Bias p=0.4466
- **qwen** (code, direct): FPR Bias p=1.0000 | FNR Bias p=1.0000
- **deepseek** (code, rubric): FPR Bias p=1.0000 | FNR Bias p=1.0000

## 6b. Statistical Bias — Fuzz-Adjusted (Corrected Ground Truth)
*Same analysis as Section 6 but using fuzz-adjusted ground truth for the code domain. Rows where the fuzzer found a `REFERENCE_BUG` (reference was wrong) or `BUG_CONFIRMED` (candidate had a real bug) are reclassified before computing FPR/FNR. For math and science domains the adjusted numbers are identical to raw. Differences between raw and adjusted in code domain reflect the impact of oracle corrections.*

### Top 3 Highest Adjusted Self-Preservation Biases (Adj FPR Gap)
![Adj FPR Bias Plot](../../../plots/actual/code/actual_code_adj_fpr_self_bias.png)

- **qwen** (code, direct): **+1.6%** adjusted bias
- **deepseek** (code, rubric): **+0.4%** adjusted bias
- **mistral** (code, cot): **+0.3%** adjusted bias

### Top 3 Highest Adjusted Self-Doubt Biases (Adj FNR Gap)
![Adj FNR Bias Plot](../../../plots/actual/code/actual_code_adj_fnr_self_bias.png)

- **llama** (code, cot): **+2.4%** adjusted bias
- **llama** (code, rubric): **+1.2%** adjusted bias
- **deepseek** (code, direct): **+0.7%** adjusted bias

### Statistical Significance (P-Values for Adjusted Bias)
- **qwen** (code, direct): Adj FPR Bias p=0.7217 | Adj FNR Bias p=1.0000
- **deepseek** (code, rubric): Adj FPR Bias p=1.0000 | Adj FNR Bias p=0.8624
- **mistral** (code, cot): Adj FPR Bias p=1.0000 | Adj FNR Bias p=0.1457

Full adjusted bias table: `actual_code_adj_bias_metrics.csv`.

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

Full table: `actual_code_domain_validity_checks.csv`.

### Code: Execution Grounding
*Instances where the code passed the test suite, but the verifier LLM overrode that execution signal and marked it INCORRECT.*
- **Total Overrides**: 1458 out of 15120 passing submissions.

#### By Verifier Model and Strategy
*Overrides, and their share of the passing submissions in that cell.*

| Verifier | cot | direct | rubric | All |
|---|---:|---:|---:|---:|
| deepseek | 45 (3.6%) | 49 (3.9%) | 43 (3.4%) | 137 (3.6%) |
| llama | 59 (4.7%) | 55 (4.4%) | 62 (4.9%) | 176 (4.7%) |
| mistral | 450 (35.7%) | 31 (2.5%) | 610 (48.4%) | 1091 (28.9%) |
| qwen | 21 (1.7%) | 18 (1.4%) | 15 (1.2%) | 54 (1.4%) |

### Science: Option Extraction Audit
*Science grading uses the shared correctness metrics above, with an additional parser audit because GPQA answers must map cleanly to one of A-D.*
*(No science domain data present)*

### Math: Answer Matching
*(No math domain data present)*

## 8. Belief vs. Reality (Told Frame vs. Actual Authorship)
*Answers Primary Question 1: does TELLING a verifier 'you wrote this' change its accuracy, independent of whether that's true? Rows below cross the told frame against ground-truth authorship (actual_source).*

| Verifier | Told Frame | Actually Self-Authored? | Accuracy | FPR |
|---|---|---|---|---|
| deepseek | other | No | 90.9% | 18.3% |
| deepseek | other | Yes | 89.1% | 44.8% |
| deepseek | self | No | 90.8% | 17.0% |
| deepseek | self | Yes | 89.1% | 46.0% |
| llama | other | No | 90.7% | 20.1% |
| llama | other | Yes | 87.1% | 33.3% |
| llama | self | No | 91.0% | 14.5% |
| llama | self | Yes | 89.3% | 26.2% |
| mistral | other | No | 75.7% | 6.2% |
| mistral | other | Yes | 82.0% | 6.0% |
| mistral | self | No | 78.1% | 6.2% |
| mistral | self | Yes | 83.1% | 7.5% |
| qwen | other | No | 92.4% | 18.6% |
| qwen | other | Yes | 91.3% | 29.7% |
| qwen | self | No | 93.3% | 16.8% |
| qwen | self | Yes | 92.0% | 27.0% |

Read this as 2x2 per verifier: (told self / actually self) vs (told self / actually other) vs (told other / actually self) vs (told other / actually other). A gap between the first two rows (same actual authorship, different label) isolates the pure *belief* effect. A gap between rows 1 and 3 (same label, different truth) isolates the pure *reality* effect. Full data: `actual_code_belief_vs_reality.csv`.

## 9. Confusion Matrices (Visuals & Raw Data)
### deepseek
**True Positives:** 3623 | **False Positives:** 380 | **True Negatives:** 1240 | **False Negatives:** 157

![Confusion Matrix deepseek](../../../plots/actual/code/actual_code_confusion_matrix_deepseek.png)
### llama
**True Positives:** 3582 | **False Positives:** 349 | **True Negatives:** 1271 | **False Negatives:** 198

![Confusion Matrix llama](../../../plots/actual/code/actual_code_confusion_matrix_llama.png)
### mistral
**True Positives:** 2667 | **False Positives:** 106 | **True Negatives:** 1514 | **False Negatives:** 1113

![Confusion Matrix mistral](../../../plots/actual/code/actual_code_confusion_matrix_mistral.png)
### qwen
**True Positives:** 3702 | **False Positives:** 320 | **True Negatives:** 1300 | **False Negatives:** 78

![Confusion Matrix qwen](../../../plots/actual/code/actual_code_confusion_matrix_qwen.png)
