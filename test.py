matched_cols = [
    #'Merchant City',
    #'Account Identifier',
    'Authorization Identifier',
    #'Authorization Date',
    #'Acct ID Last 4',
    #'Merchant Country Code',
    #'Merchant Identifier',
    #'Entry Mode Code',
    #'Merchant Name',
    #'Authorization Amount',
    #'Merchant Category Code'
]

df_confirmed_clean = df_confirmed[
    df_confirmed['Merchant Name'].notna() &
    df_confirmed['Authorization Identifier'].notna()
]

# 3. Merge on Authorization Identifier, keep Merchant Name from both sides
matched = df_confirmed_clean.merge(
    df_analysis[matched_cols + ['Merchant Name']],
    on=matched_cols,
    how='left',
    indicator=True,
    suffixes=('_confirmed', '_analysis')
)

id_missing = matched['_merge'].eq('left_only')
id_found = matched['_merge'].eq('both')
name_mismatch = id_found & (matched['Merchant Name_confirmed'] != matched['Merchant Name_analysis'])
name_match = id_found & (matched['Merchant Name_confirmed'] == matched['Merchant Name_analysis'])

print(f"Total rows checked: {len(matched)}")
print(f"ID missing entirely (no match in df_analysis): {id_missing.sum()}")
print(f"ID found, Merchant Name matches: {name_match.sum()}")
print(f"ID found, Merchant Name MISMATCH: {name_mismatch.sum()}")


with pd.option_context("display.max_rows", 200):
    display(
        matched.loc[
            name_mismatch,
            ['Authorization Identifier', 'Merchant Name_confirmed', 'Merchant Name_analysis']
        ]
    )