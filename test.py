cutoff = pd.Timestamp("2026-02-01")

train_df = df_all[df_all["Authorization Date"] < cutoff].copy()
test_df  = df_all[df_all["Authorization Date"] >= cutoff].copy()

print(f"Train: {len(train_df)} rows")
print(f"Test:  {len(test_df)} rows")
print(f"Accounts in both: {len(set(train_df['Account Identifier']) & set(test_df['Account Identifier']))}")