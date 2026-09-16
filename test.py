X_train = train_df[NUMERICAL_FEATURES + CATEGORICAL_FEATURES]
y_train = train_df["fraud_label"]

X_test = test_df[NUMERICAL_FEATURES + CATEGORICAL_FEATURES]
y_test = test_df["fraud_label"]

print("X_train:", X_train.shape, "y_train:", y_train.shape)
print("X_test:", X_test.shape, "y_test:", y_test.shape)