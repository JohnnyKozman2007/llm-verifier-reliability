# Dynamic Executive Summary

**Total Verifications Processed:** 21600

## Highest Accuracy by Domain
![Accuracy Plot](../../../plots/actual/math/actual_math_accuracy_by_domain.png)

- **Math**: deepseek (Frame: neutral, Strategy: rubric) achieved **80.8%** accuracy (**80.8% Adjusted**).

## Model Preferences by Domain (Best Configurations)
### Math
- **deepseek**: Prefers **neutral** frame & **rubric** strategy (**80.8%**)
- **llama**: Prefers **self** frame & **cot** strategy (**78.7%**)
- **mistral**: Prefers **other** frame & **rubric** strategy (**71.2%**)
- **qwen**: Prefers **other** frame & **direct** strategy (**79.7%**)

## Strategy Performance per Model (Raw Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 80.1% | 79.4% | 80.2% |
| **llama** | 78.2% | 77.4% | 77.4% |
| **mistral** | 70.9% | 70.6% | 70.6% |
| **qwen** | 78.3% | 79.4% | 78.8% |

## Strategy Performance per Model (Adjusted Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 80.1% | 79.4% | 80.2% |
| **llama** | 78.2% | 77.4% | 77.4% |
| **mistral** | 70.9% | 70.6% | 70.6% |
| **qwen** | 78.3% | 79.4% | 78.8% |

## 1. Comprehensive Accuracy Breakdown (Raw)
### Overall Average Across Everything
- **Overall**: 76.8%
### By Domain
- **Math**: 76.8%
### By Strategy
- **cot**: 76.9%
- **direct**: 76.7%
- **rubric**: 76.7%
### By Ownership Frame
- **neutral**: 76.6%
- **other**: 76.8%
- **self**: 76.9%
### By Model
- **deepseek**: 79.9%
- **llama**: 77.7%
- **mistral**: 70.7%
- **qwen**: 78.8%
### Top 3 Best Ownership + Strategy Combos
- **self + cot**: 77.1%
- **other + rubric**: 76.8%
- **other + cot**: 76.8%

## 1b. Comprehensive Accuracy Breakdown (Adjusted)
### Overall Average Across Everything
- **Overall**: 76.8%
### By Domain
- **Math**: 76.8%
### By Strategy
- **cot**: 76.9%
- **direct**: 76.7%
- **rubric**: 76.7%
### By Ownership Frame
- **neutral**: 76.6%
- **other**: 76.8%
- **self**: 76.9%
### By Model
- **deepseek**: 79.9%
- **llama**: 77.7%
- **mistral**: 70.7%
- **qwen**: 78.8%
### Top 3 Best Ownership + Strategy Combos
- **self + cot**: 77.1%
- **other + rubric**: 76.8%
- **other + cot**: 76.8%

## 2. Formatting Failure Rates (NaN / Instructions Missed)
### Overall Average Across Everything
- **Overall**: 0.0%
### By Domain
- **Math**: 0.0%
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
- **Overall**: 180.0
### By Domain
- **Math**: 180.0
### By Strategy
- **cot**: 285.9
- **direct**: 0.0
- **rubric**: 254.0
### By Ownership Frame
- **neutral**: 180.2
- **other**: 179.8
- **self**: 179.9
### By Model
- **deepseek**: 174.7
- **llama**: 239.6
- **mistral**: 149.5
- **qwen**: 156.1
### Top 3 Best Ownership + Strategy Combos
- **other + cot**: 287.0
- **neutral + cot**: 285.8
- **self + cot**: 285.1

## 5. Verifier Behavior Rates
### Overall Averages
- **Overall** -> Caught: 36.5% | Passed: 63.5% | Introduced: 4.8% | Confirmed: 95.2%
### By Domain
- **math** -> Caught: 36.5% | Passed: 63.5% | Introduced: 4.8% | Confirmed: 95.2%
### By Strategy
- **cot** -> Caught: 36.6% | Passed: 63.4% | Introduced: 4.7% | Confirmed: 95.3%
- **direct** -> Caught: 34.6% | Passed: 65.4% | Introduced: 4.1% | Confirmed: 95.9%
- **rubric** -> Caught: 38.2% | Passed: 61.8% | Introduced: 5.7% | Confirmed: 94.3%
### By Ownership Frame
- **neutral** -> Caught: 35.3% | Passed: 64.7% | Introduced: 4.5% | Confirmed: 95.5%
- **other** -> Caught: 37.3% | Passed: 62.7% | Introduced: 5.2% | Confirmed: 94.8%
- **self** -> Caught: 36.7% | Passed: 63.3% | Introduced: 4.8% | Confirmed: 95.2%
### By Model
- **deepseek** -> Caught: 56.0% | Passed: 44.0% | Introduced: 9.2% | Confirmed: 90.8%
- **llama** -> Caught: 33.5% | Passed: 66.5% | Introduced: 2.2% | Confirmed: 97.8%
- **mistral** -> Caught: 13.5% | Passed: 86.5% | Introduced: 3.2% | Confirmed: 96.8%
- **qwen** -> Caught: 42.8% | Passed: 57.2% | Introduced: 4.7% | Confirmed: 95.3%

## 6. Statistical Bias (Self vs Other)
### Top 3 Highest Self-Preservation Biases (FPR Gap)
*These models were most likely to falsely approve their own mistakes.*
![FPR Bias Plot](../../../plots/actual/math/actual_math_fpr_self_bias.png)

- **mistral** (math, rubric): **+4.8%** bias
- **deepseek** (math, rubric): **+3.2%** bias
- **mistral** (math, cot): **+3.2%** bias

### Top 3 Highest Self-Doubt Biases (FNR Gap)
*These models were most likely to falsely reject their own correct answers.*
![FNR Bias Plot](../../../plots/actual/math/actual_math_fnr_self_bias.png)

- **deepseek** (math, direct): **+0.7%** bias
- **deepseek** (math, rubric): **+0.7%** bias
- **llama** (math, rubric): **+-0.2%** bias

### Statistical Significance (P-Values for Bias) — Raw numbers, chi-square per (verifier, domain, strategy) cell.
*Small pilot sample sizes (~20/cell) mean most will read as not significant; that's expected at this scale.*
- **mistral** (math, rubric): FPR Bias p=0.2865 | FNR Bias p=0.8794
- **deepseek** (math, rubric): FPR Bias p=0.5976 | FNR Bias p=0.8257
- **mistral** (math, cot): FPR Bias p=0.4689 | FNR Bias p=0.4495

## 6b. Statistical Bias — Fuzz-Adjusted (Corrected Ground Truth)
*Same analysis as Section 6 but using fuzz-adjusted ground truth for the code domain. Rows where the fuzzer found a `REFERENCE_BUG` (reference was wrong) or `BUG_CONFIRMED` (candidate had a real bug) are reclassified before computing FPR/FNR. For math and science domains the adjusted numbers are identical to raw. Differences between raw and adjusted in code domain reflect the impact of oracle corrections.*

### Top 3 Highest Adjusted Self-Preservation Biases (Adj FPR Gap)
![Adj FPR Bias Plot](../../../plots/actual/math/actual_math_adj_fpr_self_bias.png)

- **mistral** (math, rubric): **+4.8%** adjusted bias
- **deepseek** (math, rubric): **+3.2%** adjusted bias
- **mistral** (math, cot): **+3.2%** adjusted bias

### Top 3 Highest Adjusted Self-Doubt Biases (Adj FNR Gap)
![Adj FNR Bias Plot](../../../plots/actual/math/actual_math_adj_fnr_self_bias.png)

- **deepseek** (math, direct): **+0.7%** adjusted bias
- **deepseek** (math, rubric): **+0.7%** adjusted bias
- **llama** (math, rubric): **+-0.2%** adjusted bias

### Statistical Significance (P-Values for Adjusted Bias)
- **mistral** (math, rubric): Adj FPR Bias p=0.2865 | Adj FNR Bias p=0.8794
- **deepseek** (math, rubric): Adj FPR Bias p=0.5976 | Adj FNR Bias p=0.8257
- **mistral** (math, cot): Adj FPR Bias p=0.4689 | Adj FNR Bias p=0.4495

Full adjusted bias table: `actual_math_adj_bias_metrics.csv`.

## 6c. Oracle & Fuzzing Statistics (Code Domain)
*These rows represent code verifications where the verifier overrode a passing execution result (i.e. test passed but verifier said incorrect). The fuzzer ran differential testing on each and an LLM oracle adjudicated mismatches. This section quantifies how often the verifier was right vs. wrong, and how often the benchmark reference itself was the problem.*

*(No code domain data present)*


## 7. Domain-Specific Validity Checks
*These checks are diagnostic safeguards around domain-specific grading. They support the shared metrics above; they do not replace the common accuracy/FPR/FNR analysis.*

Full table: `actual_math_domain_validity_checks.csv`.

### Code: Execution Grounding
*Instances where the code passed the test suite, but the verifier LLM overrode that execution signal and marked it INCORRECT.*
*(No code domain data present)*

### Science: Option Extraction Audit
*Science grading uses the shared correctness metrics above, with an additional parser audit because GPQA answers must map cleanly to one of A-D.*
*(No science domain data present)*

### Math: Answer Matching
- Math candidates are graded by boxed-answer extraction first, then numeric/exact matching. Symbolically equivalent but differently formatted answers remain a limitation to mention in the paper.
- **Math Verification Rows**: 21600

## 8. Belief vs. Reality (Told Frame vs. Actual Authorship)
*Answers Primary Question 1: does TELLING a verifier 'you wrote this' change its accuracy, independent of whether that's true? Rows below cross the told frame against ground-truth authorship (actual_source).*

| Verifier | Told Frame | Actually Self-Authored? | Accuracy | FPR |
|---|---|---|---|---|
| deepseek | other | No | 80.4% | 39.3% |
| deepseek | other | Yes | 79.1% | 56.6% |
| deepseek | self | No | 79.8% | 40.9% |
| deepseek | self | Yes | 78.9% | 57.4% |
| llama | other | No | 74.4% | 64.7% |
| llama | other | Yes | 85.8% | 86.7% |
| llama | self | No | 75.8% | 61.9% |
| llama | self | Yes | 86.2% | 83.3% |
| mistral | other | No | 76.7% | 84.7% |
| mistral | other | Yes | 53.3% | 84.4% |
| mistral | self | No | 76.8% | 86.9% |
| mistral | self | Yes | 51.8% | 87.7% |
| qwen | other | No | 80.5% | 48.1% |
| qwen | other | Yes | 74.4% | 81.1% |
| qwen | self | No | 80.3% | 50.2% |
| qwen | self | Yes | 75.3% | 78.8% |

Read this as 2x2 per verifier: (told self / actually self) vs (told self / actually other) vs (told other / actually self) vs (told other / actually other). A gap between the first two rows (same actual authorship, different label) isolates the pure *belief* effect. A gap between rows 1 and 3 (same label, different truth) isolates the pure *reality* effect. Full data: `actual_math_belief_vs_reality.csv`.

## 9. Confusion Matrices (Visuals & Raw Data)
### deepseek
**True Positives:** 3367 | **False Positives:** 745 | **True Negatives:** 947 | **False Negatives:** 341

![Confusion Matrix deepseek](../../../plots/actual/math/actual_math_confusion_matrix_deepseek.png)
### llama
**True Positives:** 3627 | **False Positives:** 1125 | **True Negatives:** 567 | **False Negatives:** 81

![Confusion Matrix llama](../../../plots/actual/math/actual_math_confusion_matrix_llama.png)
### mistral
**True Positives:** 3589 | **False Positives:** 1464 | **True Negatives:** 228 | **False Negatives:** 119

![Confusion Matrix mistral](../../../plots/actual/math/actual_math_confusion_matrix_mistral.png)
### qwen
**True Positives:** 3532 | **False Positives:** 967 | **True Negatives:** 725 | **False Negatives:** 176

![Confusion Matrix qwen](../../../plots/actual/math/actual_math_confusion_matrix_qwen.png)
