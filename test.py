train_fraud_rate = train_df["fraud_label"].mean()
test_fraud_rate = test_df["fraud_label"].mean()

print(f"Train fraud rate: {train_fraud_rate:.4%} ({train_df['fraud_label'].sum()} fraud / {len(train_df)} rows)")
print(f"Test fraud rate:  {test_fraud_rate:.4%} ({test_df['fraud_label'].sum()} fraud / {len(test_df)} rows)")