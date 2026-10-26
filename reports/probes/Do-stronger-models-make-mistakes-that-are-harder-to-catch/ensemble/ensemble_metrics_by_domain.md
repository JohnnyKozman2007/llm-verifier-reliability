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
| `cot` | **1-of-3** | **65.4%** | 81.5% | 31.8% | 99.1% | 68.2% | 80.5% | 0.8882 | deepseek (79.3%) |
| `cot` | **2-of-3** | **72.1%** | 84.0% | 47.3% | 96.9% | 52.7% | 84.0% | 0.8997 | deepseek (79.3%) |
| `cot` | **3-of-3** | **79.0%** | 84.5% | 67.6% | 90.5% | 32.4% | 88.8% | 0.8965 | deepseek (79.3%) |

## Domain: CODE

| Strategy | Decision Rule | Balanced Accuracy | Raw Accuracy | Catch (TNR) | Confirm (TPR) | FPR | Precision | F1 | Best Single Judge |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `cot` | **1-of-3** | **78.6%** | 86.7% | 58.3% | 98.8% | 41.7% | 84.7% | 0.9121 | llama (89.9%) |
| `cot` | **2-of-3** | **92.3%** | 93.7% | 88.9% | 95.7% | 11.1% | 95.3% | 0.9549 | llama (89.9%) |
| `cot` | **3-of-3** | **81.1%** | 74.2% | 98.3% | 63.8% | 1.7% | 98.9% | 0.7757 | llama (89.9%) |

