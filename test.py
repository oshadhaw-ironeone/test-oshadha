cutoff_val  = pd.Timestamp("2026-03-01")   # adjust to whatever split point you want
cutoff_test = pd.Timestamp("2026-04-07")

train_df = df[df["Authorization Date"] < cutoff_val].copy()
val_df   = df[(df["Authorization Date"] >= cutoff_val) & (df["Authorization Date"] < cutoff_test)].copy()
test_df  = df[df["Authorization Date"] >= cutoff_test].copy()

print(f"Train: {len(train_df)} rows")
print(f"Val:   {len(val_df)} rows")
print(f"Test:  {len(test_df)} rows")

train_fraud_rate = train_df["fraud_label"].mean()
val_fraud_rate   = val_df["fraud_label"].mean()
test_fraud_rate  = test_df["fraud_label"].mean()

print(f"Train fraud rate: {train_fraud_rate:.4%} ({train_df['fraud_label'].sum()} fraud / {len(train_df)} rows)")
print(f"Val fraud rate:   {val_fraud_rate:.4%} ({val_df['fraud_label'].sum()} fraud / {len(val_df)} rows)")
print(f"Test fraud rate:  {test_fraud_rate:.4%} ({test_df['fraud_label'].sum()} fraud / {len(test_df)} rows)")


FEATURES = NUMERICAL + CATEGORICAL   # adjust to whatever your feature list variable is called
TARGET   = "fraud_label"

X_train, y_train = train_df[FEATURES], train_df[TARGET]
X_val,   y_val   = val_df[FEATURES],   val_df[TARGET]
X_test,  y_test  = test_df[FEATURES],  test_df[TARGET]

print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"X_val:   {X_val.shape}, y_val:   {y_val.shape}")
print(f"X_test:  {X_test.shape}, y_test:  {y_test.shape}")