results = []

for col in candidate_cols:
    # Drop rows where this column is null in df_confirmed (can't compare nulls)
    df_confirmed_clean = df_confirmed[df_confirmed[col].notna()]

    matched = df_confirmed_clean.merge(
        df_analysis[[col]],
        on=col,
        how='left',
        indicator=True
    )

    matched['is_match'] = matched['_merge'].eq('both')
    counts = matched['is_match'].value_counts()

    true_count = counts.get(True, 0)
    false_count = counts.get(False, 0)
    total = true_count + false_count
    match_rate = true_count / total if total else 0

    results.append({
        'column': col,
        'true': true_count,
        'false': false_count,
        'total_compared': total,
        'match_rate': match_rate
    })

    print(f"{col:35} | True: {true_count:6} | False: {false_count:6} | Match rate: {match_rate:.2%}")

# Clean summary table sorted by best match rate
results_df = pd.DataFrame(results).sort_values('match_rate', ascending=False)
results_df