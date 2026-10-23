import json
import os
import csv
from collections import defaultdict

def generate_report():
    traces = []
    trace_file = 'reports/probes/structural_self_preference/self_preference_traces.jsonl'
    
    if not os.path.exists(trace_file):
        print(f"Error: {trace_file} not found.")
        return

    with open(trace_file, 'r') as f:
        for line in f:
            if line.strip():
                traces.append(json.loads(line))

    # The pool was drawn with the labels at probe time. Keep only pairs that are still both
    # wrong under the current grades, so a regrade cannot leave correct answers in it.
    grades = {}
    grades_dir = 'reports/probes/Do-stronger-models-make-mistakes-that-are-harder-to-catch'
    for dom in ['code', 'math', 'science']:
        with open(os.path.join(grades_dir, f'graded_{dom}.json')) as f:
            grades.update(json.load(f))
    n_probed = len({t['item_id'] for t in traces})
    traces = [t for t in traces
              if not grades[f"{t['item_id']}|deepseek"] and not grades[f"{t['item_id']}|qwen"]]
    n_kept = len({t['item_id'] for t in traces})

    md_output_path = 'reports/probes/structural_self_preference/self_preference_domain_breakdown.md'
    csv_output_path = 'reports/probes/structural_self_preference/self_preference_domain_breakdown.csv'
    
    md_content = "# Structural Self-Preference Metrics (Domain Breakdown)\n\n"
    md_content += ("Each item counts once. Its repeats are the identical prompt re-sent once per main-grid "
                   "cell it qualified in, so counts are item-equivalents averaged over those repeats. "
                   "Every row is two API calls (candidate order swapped). "
                   f"{n_kept} of the {n_probed} probed items are still both wrong under the current "
                   "grades; the rest are excluded.\n\n")
    csv_rows = [['Verifier', 'Domain', 'Items', 'Rows', 'API Calls', 'Selected OWN (%)', 'Selected OWN (Count)',
                 'Selected OTHER (%)', 'Selected OTHER (Count)', 
                 'Both Incorrect (%)', 'Both Incorrect (Count)', 
                 'Both Correct (%)', 'Both Correct (Count)', 
                 'Position Bias (%)', 'Position Bias (Count)', 
                 'Inconsistent (%)', 'Inconsistent (Count)']]

    for verifier in ['deepseek', 'qwen']:
        v_traces = [t for t in traces if t['verifier'] == verifier]
        domains = ['ALL'] + sorted(list(set(t['domain'] for t in v_traces)))
        
        md_content += f"## VERIFIER: {verifier.upper()}\n"
        
        for d in domains:
            if d == 'ALL':
                d_traces = v_traces
            else:
                d_traces = [t for t in v_traces if t['domain'] == d]
                
            by_item = defaultdict(list)
            for r in d_traces:
                by_item[r['item_id']].append(r['category'])
            total = len(by_item)
            if total == 0: continue
            n_rows = len(d_traces)

            def count(*cats):
                return sum(sum(c in cats for c in cs) / len(cs) for cs in by_item.values())

            pref_own_tag = f"TRUE_PREF_{verifier.upper()}"
            pref_other_tag = "TRUE_PREF_QWEN" if verifier == 'deepseek' else "TRUE_PREF_DEEPSEEK"

            pref_own = count(pref_own_tag)
            pref_other = count(pref_other_tag)
            both_inc = count('CONSISTENT_BOTH_INCORRECT')
            both_cor = count('CONSISTENT_BOTH_CORRECT')
            bias = count('POSITION_BIAS_ALWAYS_A', 'POSITION_BIAS_ALWAYS_B')
            inconsistent = count('INCONSISTENT')

            # Format Markdown
            md_content += f"### Domain: {d.upper()} ({total} items, {n_rows} rows, {2 * n_rows} API calls)\n"
            md_content += f"- **Selected its OWN algorithm:** {pref_own/total*100:.1f}% ({pref_own:.1f})\n"
            md_content += f"- **Selected the OTHER algorithm:** {pref_other/total*100:.1f}% ({pref_other:.1f})\n"
            md_content += f"- **Consistently voted 'Both Incorrect':** {both_inc/total*100:.1f}% ({both_inc:.1f})\n"
            md_content += f"- **Consistently voted 'Both Correct':** {both_cor/total*100:.1f}% ({both_cor:.1f})\n"
            md_content += f"- **Failed due to Position Bias (A/B):** {bias/total*100:.1f}% ({bias:.1f})\n"
            md_content += f"- **Inconsistent / Tie / Refusal:** {inconsistent/total*100:.1f}% ({inconsistent:.1f})\n\n"

            # Format CSV Row
            csv_rows.append([
                verifier.upper(), d.upper(), total, n_rows, 2 * n_rows,
                f"{pref_own/total*100:.1f}%", f"{pref_own:.1f}",
                f"{pref_other/total*100:.1f}%", f"{pref_other:.1f}",
                f"{both_inc/total*100:.1f}%", f"{both_inc:.1f}",
                f"{both_cor/total*100:.1f}%", f"{both_cor:.1f}",
                f"{bias/total*100:.1f}%", f"{bias:.1f}",
                f"{inconsistent/total*100:.1f}%", f"{inconsistent:.1f}"
            ])
            
    with open(md_output_path, 'w') as f:
        f.write(md_content)
        
    with open(csv_output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)
        
    print(f"[SUCCESS] Breakdown reports generated at:")
    print(f"  - {md_output_path}")
    print(f"  - {csv_output_path}")

if __name__ == '__main__':
    generate_report()
