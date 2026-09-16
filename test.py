train_cutoff = pd.Timestamp("2026-02-01")
test_start   = pd.Timestamp("2026-02-15")  # 2-week embargo gap

train_accounts = acct_span[acct_span["max"] < train_cutoff].index
test_accounts  = acct_span[acct_span["min"] >= test_start].index  # fully new accounts only

train_df = df_all[df_all["Account Identifier"].isin(train_accounts)]
test_df  = df_all[df_all["Account Identifier"].isin(test_accounts)]

print(f"Train: {len(train_df)} rows, {len(train_accounts)} accounts")
print(f"Test:  {len(test_df)} rows, {len(test_accounts)} accounts")
print(f"Dropped (straddling accounts): {6402 - len(train_accounts) - len(test_accounts)}")