# Original Paper Ensemble Probe: Per-Domain Metrics Specification

Leave-one-out 3-judge panel (evaluating candidates with non-author models).

## Domain: SCIENCE

| Strategy | Decision Rule | Balanced Accuracy | Raw Accuracy | Catch (TNR) | Confirm (TPR) | FPR | Precision | F1 | Best Single Judge |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `cot` | **1-of-3** | **57.3%** | 53.3% | 23.3% | 91.3% | 76.7% | 48.4% | 0.6325 | deepseek (62.8%) |
| `cot` | **2-of-3** | **60.1%** | 58.1% | 43.0% | 77.3% | 57.0% | 51.6% | 0.6191 | deepseek (62.8%) |
| `cot` | **3-of-3** | **62.1%** | 62.8% | 67.8% | 56.4% | 32.2% | 58.0% | 0.5720 | deepseek (62.8%) |

## Domain: MATH

| Strategy | Decision Rule | Balanced Accuracy | Raw Accuracy | Catch (TNR) | Confirm (TPR) | FPR | Precision | F1 | Best Single Judge |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `cot` | **1-of-3** | **62.8%** | 76.6% | 26.7% | 99.0% | 73.3% | 75.1% | 0.8540 | deepseek (74.6%) |
| `cot` | **2-of-3** | **68.2%** | 79.1% | 39.8% | 96.7% | 60.2% | 78.2% | 0.8646 | deepseek (74.6%) |
| `cot` | **3-of-3** | **73.3%** | 79.6% | 56.8% | 89.8% | 43.2% | 82.3% | 0.8589 | deepseek (74.6%) |

## Domain: CODE

| Strategy | Decision Rule | Balanced Accuracy | Raw Accuracy | Catch (TNR) | Confirm (TPR) | FPR | Precision | F1 | Best Single Judge |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `cot` | **1-of-3** | **78.6%** | 86.7% | 58.3% | 98.8% | 41.7% | 84.7% | 0.9121 | llama (89.9%) |
| `cot` | **2-of-3** | **92.3%** | 93.7% | 88.9% | 95.7% | 11.1% | 95.3% | 0.9549 | llama (89.9%) |
| `cot` | **3-of-3** | **81.1%** | 74.2% | 98.3% | 63.8% | 1.7% | 98.9% | 0.7757 | llama (89.9%) |

