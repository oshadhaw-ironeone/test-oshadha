# How many unique accounts, and how many transactions per account
acct_counts = df_all.groupby("Account Identifier").size()
print(acct_counts.describe())

# Does an account's activity span the whole time range or a narrow window?
acct_span = df_all.groupby("Account Identifier")["Authorization Date"].agg(["min", "max"])
acct_span["span_days"] = (acct_span["max"] - acct_span["min"]).dt.days
print(acct_span["span_days"].describe())

# Fraud rate over time (weekly or monthly)
fraud_rate_over_time = df_all.set_index("Authorization Date").resample("W")["fraud_label"].mean()
fraud_rate_over_time.plot(title="Fraud rate over time")