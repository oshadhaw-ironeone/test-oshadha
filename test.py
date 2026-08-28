# Get IDs that matched on Authorization Identifier alone
id_matches = df_y[df_y["Authorization Identifier"].isin(df["Authorization Identifier"])]

# Of those, which did NOT make it into the full key match?
key_matches = df_y["transaction_match_key"].isin(df["transaction_match_key"])
failed = id_matches[~key_matches]

print(f"Matched on ID but failed full key: {len(failed)}")

# Pick one example and compare both sides directly
sample_id = failed["Authorization Identifier"].iloc[0]

print("df_y row:")
print(df_y[df_y["Authorization Identifier"] == sample_id][["Authorization Identifier", "Merchant Name", "Transaction Amount", "transaction_match_key"]])

print("\ndf row:")
print(df[df["Authorization Identifier"] == sample_id][["Authorization Identifier", "Merchant Name", "Authorization Amount", "transaction_match_key"]])