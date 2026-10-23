# Dynamic Executive Summary

**Total Verifications Processed:** 21600

## Highest Accuracy by Domain
![Accuracy Plot](../../../plots/actual/math/actual_math_accuracy_by_domain.png)

- **Math**: deepseek (Frame: neutral, Strategy: rubric) achieved **85.0%** accuracy (**85.0% Adjusted**).

## Model Preferences by Domain (Best Configurations)
### Math
- **deepseek**: Prefers **neutral** frame & **rubric** strategy (**85.0%**)
- **llama**: Prefers **self** frame & **cot** strategy (**83.5%**)
- **mistral**: Prefers **self** frame & **direct** strategy (**76.0%**)
- **qwen**: Prefers **self** frame & **rubric** strategy (**84.3%**)

## Strategy Performance per Model (Raw Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 84.2% | 83.3% | 84.4% |
| **llama** | 83.1% | 82.2% | 82.2% |
| **mistral** | 75.4% | 75.7% | 74.9% |
| **qwen** | 82.9% | 84.0% | 83.8% |

## Strategy Performance per Model (Adjusted Accuracy)
| Model | cot | direct | rubric |
|-------|---|---|---|
| **deepseek** | 84.2% | 83.3% | 84.4% |
| **llama** | 83.1% | 82.2% | 82.2% |
| **mistral** | 75.4% | 75.7% | 74.9% |
| **qwen** | 82.9% | 84.0% | 83.8% |

## 1. Comprehensive Accuracy Breakdown (Raw)
### Overall Average Across Everything
- **Overall**: 81.4%
### By Domain
- **Math**: 81.4%
### By Strategy
- **cot**: 81.4%
- **direct**: 81.3%
- **rubric**: 81.3%
### By Ownership Frame
- **neutral**: 81.3%
- **other**: 81.3%
- **self**: 81.4%
### By Model
- **deepseek**: 84.0%
- **llama**: 82.5%
- **mistral**: 75.4%
- **qwen**: 83.6%
### Top 3 Best Ownership + Strategy Combos
- **self + cot**: 81.6%
- **neutral + cot**: 81.5%
- **other + direct**: 81.4%

## 1b. Comprehensive Accuracy Breakdown (Adjusted)
### Overall Average Across Everything
- **Overall**: 81.4%
### By Domain
- **Math**: 81.4%
### By Strategy
- **cot**: 81.4%
- **direct**: 81.3%
- **rubric**: 81.3%
### By Ownership Frame
- **neutral**: 81.3%
- **other**: 81.3%
- **self**: 81.4%
### By Model
- **deepseek**: 84.0%
- **llama**: 82.5%
- **mistral**: 75.4%
- **qwen**: 83.6%
### Top 3 Best Ownership + Strategy Combos
- **self + cot**: 81.6%
- **neutral + cot**: 81.5%
- **other + direct**: 81.4%

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
- **Overall** -> Caught: 42.6% | Passed: 57.4% | Introduced: 4.7% | Confirmed: 95.3%
### By Domain
- **math** -> Caught: 42.6% | Passed: 57.4% | Introduced: 4.7% | Confirmed: 95.3%
### By Strategy
- **cot** -> Caught: 42.7% | Passed: 57.3% | Introduced: 4.6% | Confirmed: 95.4%
- **direct** -> Caught: 40.5% | Passed: 59.5% | Introduced: 4.0% | Confirmed: 96.0%
- **rubric** -> Caught: 44.7% | Passed: 55.3% | Introduced: 5.4% | Confirmed: 94.6%
### By Ownership Frame
- **neutral** -> Caught: 41.5% | Passed: 58.5% | Introduced: 4.3% | Confirmed: 95.7%
- **other** -> Caught: 43.6% | Passed: 56.4% | Introduced: 5.0% | Confirmed: 95.0%
- **self** -> Caught: 42.9% | Passed: 57.1% | Introduced: 4.7% | Confirmed: 95.3%
### By Model
- **deepseek** -> Caught: 64.8% | Passed: 35.2% | Introduced: 9.1% | Confirmed: 90.9%
- **llama** -> Caught: 39.6% | Passed: 60.4% | Introduced: 2.0% | Confirmed: 98.0%
- **mistral** -> Caught: 15.7% | Passed: 84.3% | Introduced: 3.1% | Confirmed: 96.9%
- **qwen** -> Caught: 50.5% | Passed: 49.5% | Introduced: 4.5% | Confirmed: 95.5%

## 6. Statistical Bias (Self vs Other)
### Top 3 Highest Self-Preservation Biases (FPR Gap)
*These models were most likely to falsely approve their own mistakes.*
![FPR Bias Plot](../../../plots/actual/math/actual_math_fpr_self_bias.png)

- **mistral** (math, rubric): **+5.7%** bias
- **deepseek** (math, rubric): **+3.8%** bias
- **mistral** (math, cot): **+3.1%** bias

### Top 3 Highest Self-Doubt Biases (FNR Gap)
*These models were most likely to falsely reject their own correct answers.*
![FNR Bias Plot](../../../plots/actual/math/actual_math_fnr_self_bias.png)

- **deepseek** (math, direct): **+0.9%** bias
- **deepseek** (math, rubric): **+0.7%** bias
- **llama** (math, cot): **+-0.2%** bias

### Statistical Significance (P-Values for Bias) — Raw numbers, chi-square per (verifier, domain, strategy) cell.
*Small pilot sample sizes (~20/cell) mean most will read as not significant; that's expected at this scale.*
- **mistral** (math, rubric): FPR Bias p=0.2659 | FNR Bias p=0.8842
- **deepseek** (math, rubric): FPR Bias p=0.5389 | FNR Bias p=0.8296
- **mistral** (math, cot): FPR Bias p=0.5473 | FNR Bias p=0.3679

## 6b. Statistical Bias — Fuzz-Adjusted (Corrected Ground Truth)
*Same analysis as Section 6 but using fuzz-adjusted ground truth for the code domain. Rows where the fuzzer found a `REFERENCE_BUG` (reference was wrong) or `BUG_CONFIRMED` (candidate had a real bug) are reclassified before computing FPR/FNR. For math and science domains the adjusted numbers are identical to raw. Differences between raw and adjusted in code domain reflect the impact of oracle corrections.*

### Top 3 Highest Adjusted Self-Preservation Biases (Adj FPR Gap)
![Adj FPR Bias Plot](../../../plots/actual/math/actual_math_adj_fpr_self_bias.png)

- **mistral** (math, rubric): **+5.7%** adjusted bias
- **deepseek** (math, rubric): **+3.8%** adjusted bias
- **mistral** (math, cot): **+3.1%** adjusted bias

### Top 3 Highest Adjusted Self-Doubt Biases (Adj FNR Gap)
![Adj FNR Bias Plot](../../../plots/actual/math/actual_math_adj_fnr_self_bias.png)

- **deepseek** (math, direct): **+0.9%** adjusted bias
- **deepseek** (math, rubric): **+0.7%** adjusted bias
- **llama** (math, cot): **+-0.2%** adjusted bias

### Statistical Significance (P-Values for Adjusted Bias)
- **mistral** (math, rubric): Adj FPR Bias p=0.2659 | Adj FNR Bias p=0.8842
- **deepseek** (math, rubric): Adj FPR Bias p=0.5389 | Adj FNR Bias p=0.8296
- **mistral** (math, cot): Adj FPR Bias p=0.5473 | Adj FNR Bias p=0.3679

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
- Math candidates are graded by final-answer extraction, then exact-rational and canonical-form matching: formatting-equivalent answers (plain vs. LaTeX fractions, reduced or not, decimal equivalents, sqrt/pi notation) are accepted. Algebraically equivalent but structurally different rewrites (e.g. factored vs. expanded forms) remain a limitation to mention in the paper.
- **Math Verification Rows**: 21600

## 8. Belief vs. Reality (Told Frame vs. Actual Authorship)
*Answers Primary Question 1: does TELLING a verifier 'you wrote this' change its accuracy, independent of whether that's true? Rows below cross the told frame against ground-truth authorship (actual_source).*

| Verifier | Told Frame | Actually Self-Authored? | Accuracy | FPR |
|---|---|---|---|---|
| deepseek | other | No | 84.1% | 31.2% |
| deepseek | other | Yes | 84.4% | 46.5% |
| deepseek | self | No | 83.4% | 33.1% |
| deepseek | self | Yes | 84.2% | 47.5% |
| llama | other | No | 79.8% | 58.7% |
| llama | other | Yes | 89.1% | 87.2% |
| llama | self | No | 81.1% | 55.5% |
| llama | self | Yes | 89.6% | 82.1% |
| mistral | other | No | 81.3% | 82.5% |
| mistral | other | Yes | 57.3% | 82.3% |
| mistral | self | No | 81.8% | 84.6% |
| mistral | self | Yes | 55.3% | 86.1% |
| qwen | other | No | 85.0% | 39.6% |
| qwen | other | Yes | 79.8% | 76.9% |
| qwen | self | No | 84.8% | 42.0% |
| qwen | self | Yes | 80.7% | 74.1% |

Read this as 2x2 per verifier: (told self / actually self) vs (told self / actually other) vs (told other / actually self) vs (told other / actually other). A gap between the first two rows (same actual authorship, different label) isolates the pure *belief* effect. A gap between rows 1 and 3 (same label, different truth) isolates the pure *reality* effect. Full data: `actual_math_belief_vs_reality.csv`.

## 9. Confusion Matrices (Visuals & Raw Data)
### deepseek
**True Positives:** 3608 | **False Positives:** 504 | **True Negatives:** 927 | **False Negatives:** 361

![Confusion Matrix deepseek](../../../plots/actual/math/actual_math_confusion_matrix_deepseek.png)
### llama
**True Positives:** 3888 | **False Positives:** 864 | **True Negatives:** 567 | **False Negatives:** 81

![Confusion Matrix llama](../../../plots/actual/math/actual_math_confusion_matrix_llama.png)
### mistral
**True Positives:** 3846 | **False Positives:** 1207 | **True Negatives:** 224 | **False Negatives:** 123

![Confusion Matrix mistral](../../../plots/actual/math/actual_math_confusion_matrix_mistral.png)
### qwen
**True Positives:** 3791 | **False Positives:** 708 | **True Negatives:** 723 | **False Negatives:** 178

![Confusion Matrix qwen](../../../plots/actual/math/actual_math_confusion_matrix_qwen.png)
