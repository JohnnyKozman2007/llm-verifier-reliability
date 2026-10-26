# Causal Style Transfer Metrics (Stylistic Fingerprinting Probe)

1467 of the 2016 probed false positives are still wrong under the current grades; the rest are excluded.

## VERIFIER: DEEPSEEK
- **Total Baseline False Positives Tested:** 623
- **Original FPR:** 100.0%
- **Control FPR (Placebo Rewrite):** 79.9% (498/623)
- **Mistral Style FPR (Style Stripped):** 80.1% (499/623)
- **Net FPR Drop (Effect of Style):** +0.2%
- **McNemar exact p (style vs control):** 1.00

> **Conclusion:** Changing the prose and formatting style had no statistically significant impact on DEEPSEEK's self-bias. The 'Stylistic Fingerprinting' hypothesis is dead.

## VERIFIER: QWEN
- **Total Baseline False Positives Tested:** 844
- **Original FPR:** 100.0%
- **Control FPR (Placebo Rewrite):** 89.9% (759/844)
- **Mistral Style FPR (Style Stripped):** 87.7% (740/844)
- **Net FPR Drop (Effect of Style):** -2.3%
- **McNemar exact p (style vs control):** 0.06

> **Conclusion:** Changing the prose and formatting style had no statistically significant impact on QWEN's self-bias. The 'Stylistic Fingerprinting' hypothesis is dead.

