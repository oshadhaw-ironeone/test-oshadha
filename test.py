results = []

for col1 in df1.columns:
    vals1 = df1[col1].astype(str).str.strip()
    for col2 in df2.columns:
        vals2 = df2[col2].astype(str).str.strip()
        match_count = vals1.isin(vals2).sum()
        match_pct = match_count / len(df1) * 100
        results.append((col1, col2, match_count, match_pct))

results_df = pd.DataFrame(results, columns=['df1_col', 'df2_col', 'matches', 'match_pct'])
results_df = results_df.sort_values('match_pct', ascending=False)
print(results_df.head(20))