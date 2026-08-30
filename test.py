# ============================================================
# FULL ANALYSIS: Merchant Name vs Merchant Identifier (df_confirmed)
# ============================================================

# --- 1. Basic data quality ---
print("=== BASIC COUNTS ===")
print(f"Total rows: {len(df_confirmed)}")
print(f"Merchant Name nulls: {df_confirmed['Merchant Name'].isna().sum()}")
print(f"Merchant Identifier nulls: {df_confirmed['Merchant Identifier'].isna().sum()}")
print(f"Unique Merchant Names: {df_confirmed['Merchant Name'].nunique()}")
print(f"Unique Merchant Identifiers: {df_confirmed['Merchant Identifier'].nunique()}")

# --- 2. Clean subset (drop rows missing either field) ---
df_mi = df_confirmed[
    df_confirmed['Merchant Name'].notna() &
    df_confirmed['Merchant Identifier'].notna()
].copy()

print(f"\nRows with both fields present: {len(df_mi)}")

# --- 3. Does one Merchant Identifier map to multiple Merchant Names? ---
id_to_names = df_mi.groupby('Merchant Identifier')['Merchant Name'].nunique()
inconsistent_ids = id_to_names[id_to_names > 1]

print(f"\n=== MERCHANT IDENTIFIER -> MULTIPLE NAMES ===")
print(f"Merchant Identifiers with >1 distinct Merchant Name: {len(inconsistent_ids)}")

# Show detail for the worst offenders
inconsistent_detail = (
    df_mi[df_mi['Merchant Identifier'].isin(inconsistent_ids.index)]
    .groupby('Merchant Identifier')['Merchant Name']
    .unique()
    .reset_index()
    .rename(columns={'Merchant Name': 'Distinct Names'})
)
inconsistent_detail['Num Distinct Names'] = inconsistent_detail['Distinct Names'].apply(len)
inconsistent_detail = inconsistent_detail.sort_values('Num Distinct Names', ascending=False)

with pd.option_context("display.max_colwidth", None, "display.max_rows", 50):
    display(inconsistent_detail.head(50))

# --- 4. Does one Merchant Name map to multiple Merchant Identifiers? ---
name_to_ids = df_mi.groupby('Merchant Name')['Merchant Identifier'].nunique()
inconsistent_names = name_to_ids[name_to_ids > 1]

print(f"\n=== MERCHANT NAME -> MULTIPLE IDENTIFIERS ===")
print(f"Merchant Names with >1 distinct Merchant Identifier: {len(inconsistent_names)}")

inconsistent_names_detail = (
    df_mi[df_mi['Merchant Name'].isin(inconsistent_names.index)]
    .groupby('Merchant Name')['Merchant Identifier']
    .unique()
    .reset_index()
    .rename(columns={'Merchant Identifier': 'Distinct Identifiers'})
)
inconsistent_names_detail['Num Distinct Identifiers'] = inconsistent_names_detail['Distinct Identifiers'].apply(len)
inconsistent_names_detail = inconsistent_names_detail.sort_values('Num Distinct Identifiers', ascending=False)

with pd.option_context("display.max_colwidth", None, "display.max_rows", 50):
    display(inconsistent_names_detail.head(50))

# --- 5. Top merchants by transaction volume ---
print(f"\n=== TOP 20 MERCHANT NAMES BY ROW COUNT ===")
display(df_mi['Merchant Name'].value_counts().head(20))

print(f"\n=== TOP 20 MERCHANT IDENTIFIERS BY ROW COUNT ===")
display(df_mi['Merchant Identifier'].value_counts().head(20))

# --- 6. Summary ---
print(f"\n=== SUMMARY ===")
print(f"Total unique Merchant Identifiers: {df_mi['Merchant Identifier'].nunique()}")
print(f"Total unique Merchant Names: {df_mi['Merchant Name'].nunique()}")
print(f"Identifiers mapping to >1 Name: {len(inconsistent_ids)} ({len(inconsistent_ids)/df_mi['Merchant Identifier'].nunique():.1%})")
print(f"Names mapping to >1 Identifier: {len(inconsistent_names)} ({len(inconsistent_names)/df_mi['Merchant Name'].nunique():.1%})")
