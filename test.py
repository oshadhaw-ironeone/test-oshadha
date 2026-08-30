id_found = matched['_merge'].eq('both')
name_mismatch = id_found & (matched['Merchant Name_confirmed'] != matched['Merchant Name_analysis'])

print(f"ID missing entirely: {not_matched.sum()}")
print(f"ID found but name mismatch: {name_mismatch.sum()}")
print(f"ID found and name matches: {(id_found & ~name_mismatch.reindex(matched.index, fill_value=False)).sum()}")

with pd.option_context("display.max_rows", 20):
    display(matched.loc[name_mismatch, ['Authorization Identifier', 'Merchant Name_confirmed', 'Merchant Name_analysis']])