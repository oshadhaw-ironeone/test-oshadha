sample_id = matched_rows["Authorization Identifier"].iloc[0]

print("df_y row:")
print(df_y[df_y["Authorization Identifier"] == sample_id][["Authorization Identifier", "Merchant Name", "Authorization Amount"]])

print("\ndf row:")
print(df[df["Authorization Identifier"] == sample_id][["Authorization Identifier", "Merchant Name", "Transaction Amount"]])