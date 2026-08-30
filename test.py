matched_cols = [
    # 'Authorization Date',
    # 'Acct ID Last 4',
    # 'Merchant Country Code',
    # 'Merchant Identifier',
    # 'Entry Mode Code',
    'Merchant Name',
    # 'Authorization Amount',
    # 'Merchant Category Code'
]

df_confirmed_clean = df_confirmed[df_confirmed['Merchant Name'].notna()]

# Exclude 'Merchant Name' from the join keys so we can compare it directly
join_keys = [c for c in matched_cols if c != 'Merchant Name']

matched = df_confirmed_clean.merge(
    df_analysis[join_keys + ['Merchant Name']],
    on=join_keys,
    how='left',
    indicator=True,
    suffixes=('_confirmed', '_analysis')
)

is_not_matched = matched['_merge'].eq('left_only')
not_matched = is_not_matched  # keep the boolean mask, same as before

counts = not_matched.value_counts()
true_count = counts.get(True, 0)
false_count = counts.get(False, 0)
total = true_count + false_count
print(f"Not matched| True: {true_count} | False: {false_count}")

not_matched_rows = matched[not_matched]
print(not_matched_rows.columns.tolist())
not_matched_rows[join_keys + ['Merchant Name_confirmed', 'Merchant Name_analysis', '_merge']]