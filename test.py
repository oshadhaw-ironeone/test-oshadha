# Basic overlap: how many df_y keys exist in df
matches = df_y["transaction_match_key"].isin(df["transaction_match_key"])
print(f"Matching rows in df_y: {matches.sum()} out of {len(df_y)}")

# See the actual matched rows from df_y
matched_rows = df_y[matches]
print(matched_rows.head())