"""
Stratified Self-Preference Estimator for LLM Verifiers.

This probe evaluates the self-preference gap while holding the exact error
candidate fixed across strata, isolating true model identity from prompt framing,
difficulty, and generator quality.

Every figure is computed from the granular traces on each run and written to
reports/actual/all/stratified_estimator_summary.md; none is hard-coded here.
"""

import os
import sys
import argparse
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

def judge_fixed_gap(errors):
    """Self effect in pp holding the error AND the judge fixed, with its item-clustered SE.

    The stratum comparison holds the error fixed but not the judge, so a lenient judge's
    own errors look self-preferred whenever the other judges are stricter. This linear
    probability model adds judge (and strategy, frame) fixed effects to the error ones.
    """
    d = errors.assign(
        v=errors['verdict_num'] * 100,
        self_judge=errors['is_self'].astype(int),
        err=errors['domain'] + '|' + errors['item_id'].astype(str) + '|' + errors['generator'],
        item=errors['domain'] + '|' + errors['item_id'].astype(str),
    )
    fit = smf.ols('v ~ self_judge + C(err) + C(verifier) + C(strategy) + C(frame)', data=d).fit(
        cov_type='cluster', cov_kwds={'groups': pd.factorize(d['item'])[0]})
    return fit.params['self_judge'], fit.bse['self_judge']

def error_fixed_gap(errors):
    """Author vs other judges on the identical wrong answer, within strata of
    (item, generator, strategy, frame). Returns strata, distinct errors, the author's and
    the others' approval rates (%), the mean gap (pp) and its item-clustered SE."""
    # Group by stratum: (domain, item_id, generator, strategy, frame)
    grouped = errors.groupby(
        ['domain', 'item_id', 'generator', 'strategy', 'frame', 'is_self']
    )['verdict_num'].agg(['count', 'mean']).unstack('is_self')
    
    # Require at least one self and one other evaluation per stratum
    valid = grouped[(grouped[('count', True)] > 0) & (grouped[('count', False)] > 0)].copy()
    
    # Filter out candidate errors with sparse evaluations (< 5 valid strata out of 9)
    cand_counts = valid.groupby(level=['domain', 'item_id', 'generator']).size()
    dense = cand_counts[cand_counts >= 5].index

    # Every qualifying stratum is kept. Selecting strata by the sign of their own
    # effect would bias the quantity this estimator exists to measure.
    s_final = valid.loc[valid.index.droplevel(['strategy', 'frame']).isin(dense)].copy()
    
    n_strata = len(s_final)
    distinct_errors = len(s_final.index.droplevel(['strategy', 'frame']).drop_duplicates())
    
    diff_final = (s_final[('mean', True)] - s_final[('mean', False)]) * 100
    self_fpr = s_final[('mean', True)].mean() * 100
    other_fpr = s_final[('mean', False)].mean() * 100
    gap = diff_final.mean()
    
    # Cluster-robust standard error of the mean gap, clustered by item
    item_cluster = s_final.index.get_level_values('domain') + '_' + s_final.index.get_level_values('item_id').astype(str)
    residuals = diff_final - gap
    cluster_sums = residuals.groupby(item_cluster).sum()
    se = np.sqrt((cluster_sums ** 2).sum()) / n_strata
    return n_strata, distinct_errors, self_fpr, other_fpr, gap, se

def run_stratified_estimator(
    csv_path="reports/actual/all/actual_all_results_granular.csv",
    output_dir="reports/actual/all"
):
    if not os.path.exists(csv_path):
        print(f"Error: dataset {csv_path} not found.")
        sys.exit(1)

    print(f"Loading granular verification traces from {csv_path}...")
    df = pd.read_csv(csv_path, low_memory=False)

    # Filter to error candidates and exclude strict JSON parsing failures
    errors = df[(df['candidate_is_correct'] == False) & (df['strict_json_parse_fail'] == 0)].copy()
    errors['is_self'] = (errors['verifier'] == errors['generator'])
    errors['verdict_num'] = errors['parsed_verdict'].astype(float)
    # Mistral dropped as both generator and judge
    no_mistral = errors[(errors['generator'] != 'mistral') & (errors['verifier'] != 'mistral')]

    n_strata, distinct_errors, self_fpr, other_fpr, gap, se = error_fixed_gap(errors)
    ci_lower = gap - 1.96 * se
    ci_upper = gap + 1.96 * se
    
    print("\n" + "=" * 70)
    print("STRATIFIED SELF-PREFERENCE ESTIMATOR")
    print("=" * 70)
    print(f"Total Strata Evaluated : {n_strata:,}")
    print(f"Distinct Errors Fixed  : {distinct_errors:,}")
    print(f"Self FPR               : {self_fpr:.1f}%")
    print(f"Other FPR              : {other_fpr:.1f}%")
    print(f"Self-Preference Gap    : {gap:+.1f} pp")
    print(f"Item-Clustered SE      : {se:.2f} pp")
    print(f"95% Confidence Interval: [{ci_lower:+.1f}, {ci_upper:+.1f}]")
    print("=" * 70)

    n_strata_nm, _, _, _, gap_nm, se_nm = error_fixed_gap(no_mistral)
    print(f"\nError held fixed, without Mistral: {gap_nm:+.1f} pp  "
          f"95% CI [{gap_nm - 1.96 * se_nm:+.1f}, {gap_nm + 1.96 * se_nm:+.1f}]  ({n_strata_nm:,} strata)")

    fe_gap, fe_se = judge_fixed_gap(errors)
    fe_gap_nm, fe_se_nm = judge_fixed_gap(no_mistral)
    print("\nError AND judge held fixed (two-way fixed effects, item-clustered SE):")
    print(f"  all judges      : {fe_gap:+.1f} pp  95% CI [{fe_gap - 1.96 * fe_se:+.1f}, {fe_gap + 1.96 * fe_se:+.1f}]")
    print(f"  without Mistral : {fe_gap_nm:+.1f} pp  95% CI [{fe_gap_nm - 1.96 * fe_se_nm:+.1f}, {fe_gap_nm + 1.96 * fe_se_nm:+.1f}]")
    
    # Model Scale Breakdown (not reported in the paper).
    # Per verifier, over all of its error verdicts: its own errors vs other generators'
    # errors. Not stratum-matched, unlike the pooled gap above.
    print("\nModel Scale Breakdown (Verifier Self vs. Other, all error verdicts):")
    labels = {'deepseek': 'DeepSeek-V3 (671B)', 'qwen': 'Qwen2.5-72B (72B)',
              'llama': 'Llama-3.3-70B (70B)', 'mistral': 'Mistral-Nemo-12B (12B)'}
    model_data = {}
    for key, model_name in labels.items():
        d = errors[errors['verifier'] == key]
        s_fpr = d[d['is_self']]['verdict_num'].mean() * 100
        o_fpr = d[~d['is_self']]['verdict_num'].mean() * 100
        model_data[model_name] = {'self': s_fpr, 'other': o_fpr, 'gap': s_fpr - o_fpr}
    model_rows = []
    for model_name, stats in model_data.items():
        print(f"  - {model_name:24s}: Self FPR={stats['self']:.1f}%, Other FPR={stats['other']:.1f}%, Gap={stats['gap']:+.1f}pp")
        model_rows.append({
            'Model': model_name,
            'Self_FPR': f"{stats['self']:.1f}%",
            'Other_FPR': f"{stats['other']:.1f}%",
            'FPR_Gap': f"{stats['gap']:+.1f}pp"
        })
        
    # Output to markdown summary
    os.makedirs(output_dir, exist_ok=True)
    report_md = os.path.join(output_dir, "stratified_estimator_summary.md")
    with open(report_md, "w") as f:
        f.write("# Stratified Estimator Summary (Main Experiment)\n\n")
        f.write(f"- **Evaluated Strata**: {n_strata:,}\n")
        f.write(f"- **Distinct Errors**: {distinct_errors:,}\n")
        f.write(f"- **Self False Positive Rate (FPR)**: {self_fpr:.1f}%\n")
        f.write(f"- **Other False Positive Rate (FPR)**: {other_fpr:.1f}%\n")
        f.write(f"- **Self-Preference Gap**: {gap:+.1f} pp\n")
        f.write(f"- **Item-Clustered SE**: {se:.2f} pp\n")
        f.write(f"- **95% Confidence Interval**: [{ci_lower:+.1f}, {ci_upper:+.1f}]\n")
        f.write(f"- **Without Mistral**: {gap_nm:+.1f} pp, 95% CI [{gap_nm - 1.96 * se_nm:+.1f}, {gap_nm + 1.96 * se_nm:+.1f}] ({n_strata_nm:,} strata)\n\n")
        f.write("## Error and Judge Held Fixed\n\n")
        f.write("Two-way fixed effects (error, judge, strategy, frame), item-clustered SE.\n\n")
        f.write(f"- **All judges**: {fe_gap:+.1f} pp, 95% CI [{fe_gap - 1.96 * fe_se:+.1f}, {fe_gap + 1.96 * fe_se:+.1f}]\n")
        f.write(f"- **Without Mistral**: {fe_gap_nm:+.1f} pp, 95% CI [{fe_gap_nm - 1.96 * fe_se_nm:+.1f}, {fe_gap_nm + 1.96 * fe_se_nm:+.1f}]\n\n")
        f.write("## Model Scale Breakdown\n\n")
        f.write("| Model | Self FPR | Other FPR | FPR Gap |\n")
        f.write("|---|:---:|:---:|:---:|\n")
        for row in model_rows:
            f.write(f"| {row['Model']} | {row['Self_FPR']} | {row['Other_FPR']} | {row['FPR_Gap']} |\n")
            
    print(f"\nSaved executive summary to: {report_md}")
    return {'strata': n_strata, 'distinct_errors': distinct_errors, 'self_fpr': self_fpr,
            'other_fpr': other_fpr, 'gap': gap, 'se': se, 'per_verifier': model_data,
            'gap_no_mistral': gap_nm, 'se_no_mistral': se_nm,
            'judge_fixed_gap': fe_gap, 'judge_fixed_se': fe_se,
            'judge_fixed_gap_no_mistral': fe_gap_nm, 'judge_fixed_se_no_mistral': fe_se_nm}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stratified Self-Preference Estimator")
    parser.add_argument("--csv", default="reports/actual/all/actual_all_results_granular.csv", help="Path to granular CSV")
    parser.add_argument("--out", default="reports/actual/all", help="Output directory")
    args = parser.parse_args()
    run_stratified_estimator(args.csv, args.out)
