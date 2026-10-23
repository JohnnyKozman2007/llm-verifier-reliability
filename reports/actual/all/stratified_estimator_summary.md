# Stratified Estimator Summary (Main Experiment)

- **Evaluated Strata**: 6,014
- **Distinct Errors**: 671
- **Self False Positive Rate (FPR)**: 57.7%
- **Other False Positive Rate (FPR)**: 43.8%
- **Self-Preference Gap**: +13.9 pp
- **Item-Clustered SE**: 1.19 pp
- **95% Confidence Interval**: [+11.5, +16.2]

## Error and Judge Held Fixed

Two-way fixed effects (error, judge, strategy, frame), item-clustered SE.

- **All judges**: +11.1 pp, 95% CI [+8.9, +13.2]
- **Without Mistral**: +5.6 pp, 95% CI [+3.1, +8.1]

## Model Scale Breakdown

| Model | Self FPR | Other FPR | FPR Gap |
|---|:---:|:---:|:---:|
| DeepSeek-V3 (671B) | 51.3% | 28.6% | +22.7pp |
| Qwen2.5-72B (72B) | 62.5% | 40.5% | +22.0pp |
| Llama-3.3-70B (70B) | 52.1% | 46.9% | +5.3pp |
| Mistral-Nemo-12B (12B) | 61.6% | 62.3% | -0.7pp |
