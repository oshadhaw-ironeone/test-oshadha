fraud_only = df_all[df_all["fraud_label"] == 1]
fraud_only["label_lag_days"] = (fraud_only["Record Creation Date"] - fraud_only["Authorization Date"]).dt.days

fraud_only.groupby(fraud_only["Authorization Date"].dt.to_period("M"))["label_lag_days"].mean()



straddling_accounts = set(acct_span.index) - set(train_accounts) - set(test_accounts)

overall_fraud_rate = df_all["fraud_label"].mean()
straddling_fraud_rate = df_all[df_all["Account Identifier"].isin(straddling_accounts)]["fraud_label"].mean()

print(f"Overall fraud rate: {overall_fraud_rate:.3f}")
print(f"Dropped-accounts fraud rate: {straddling_fraud_rate:.3f}")