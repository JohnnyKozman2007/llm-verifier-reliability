import json
import os
import csv
from scipy.stats import binomtest

def generate_report():
    trace_file = 'reports/probes/style_transfer/style_transfer_traces.jsonl'
    md_output_path = 'reports/probes/style_transfer/style_transfer_breakdown.md'
    csv_output_path = 'reports/probes/style_transfer/style_transfer_breakdown.csv'
    
    if not os.path.exists(trace_file):
        print(f"Error: {trace_file} not found.")
        return

    traces = []
    with open(trace_file, 'r') as f:
        for line in f:
            if line.strip():
                traces.append(json.loads(line))

    # The pool was drawn with the labels at probe time. Keep only answers that are still
    # wrong under the current grades, so a regrade cannot leave correct answers in it.
    grades = {}
    grades_dir = 'reports/probes/Do-stronger-models-make-mistakes-that-are-harder-to-catch'
    for dom in ['code', 'math', 'science']:
        with open(os.path.join(grades_dir, f'graded_{dom}.json')) as f:
            grades.update(json.load(f))
    n_probed = len(traces)
    traces = [t for t in traces if not grades[f"{t['item_id']}|{t['verifier']}"]]

    md_content = "# Causal Style Transfer Metrics (Stylistic Fingerprinting Probe)\n\n"
    md_content += (f"{len(traces)} of the {n_probed} probed false positives are still wrong under the "
                   "current grades; the rest are excluded.\n\n")
    csv_rows = [['Verifier', 'Total False Positives Tested', 'Original FPR', 'Control FPR', 'Mistral Style FPR', 'FPR Drop (Causal Effect)', 'McNemar p']]

    for verifier in ['deepseek', 'qwen']:
        v_traces = [t for t in traces if t['verifier'] == verifier]
        total = len(v_traces)
        if total == 0: continue
        
        # Original FPR is 100% because we specifically only tested False Positives
        original_fpr = 100.0
        
        # Control FPR: The engine's baseline when told to keep the original style
        control_fp_count = sum(1 for t in v_traces if t['control_verdict'] == True)
        control_fpr = (control_fp_count / total) * 100 if total > 0 else 0
        
        # Mistral FPR: The engine's FPR when the style was changed to Mistral
        mistral_fp_count = sum(1 for t in v_traces if t['mistral_style_verdict'] == True)
        mistral_fpr = (mistral_fp_count / total) * 100 if total > 0 else 0
        
        # The true causal drop in bias caused by stripping the style
        fpr_drop = mistral_fpr - control_fpr

        # Exact McNemar test on the paired verdicts for the same case
        b = sum(1 for t in v_traces if t['control_verdict'] == True and t['mistral_style_verdict'] != True)
        c = sum(1 for t in v_traces if t['control_verdict'] != True and t['mistral_style_verdict'] == True)
        p_value = binomtest(b, b + c, 0.5).pvalue if b + c else 1.0

        md_content += f"## VERIFIER: {verifier.upper()}\n"
        md_content += f"- **Total Baseline False Positives Tested:** {total}\n"
        md_content += f"- **Original FPR:** {original_fpr:.1f}%\n"
        md_content += f"- **Control FPR (Placebo Rewrite):** {control_fpr:.1f}% ({control_fp_count}/{total})\n"
        md_content += f"- **Mistral Style FPR (Style Stripped):** {mistral_fpr:.1f}% ({mistral_fp_count}/{total})\n"
        md_content += f"- **Net FPR Drop (Effect of Style):** {fpr_drop:+.1f}%\n"
        md_content += f"- **McNemar exact p (style vs control):** {p_value:.2f}\n\n"

        if p_value >= 0.05:
            md_content += f"> **Conclusion:** Changing the prose and formatting style had no statistically significant impact on {verifier.upper()}'s self-bias. The 'Stylistic Fingerprinting' hypothesis is dead.\n\n"

        csv_rows.append([
            verifier.upper(), total,
            f"{original_fpr:.1f}%", f"{control_fpr:.1f}%", f"{mistral_fpr:.1f}%", f"{fpr_drop:+.1f}%", f"{p_value:.2f}"
        ])

    with open(md_output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)
        
    print(f"[SUCCESS] Style Transfer reports generated at:")
    print(f"  - {md_output_path}")
    print(f"  - {csv_output_path}")

if __name__ == '__main__':
    generate_report()
