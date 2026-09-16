import pandas as pd

date_min = df["Authorization Date"].min()
date_max = df["Authorization Date"].max()

candidate_cutoffs = pd.date_range(date_min, date_max, freq="W")

results = []
for cutoff in candidate_cutoffs:
    train = df[df["Authorization Date"] < cutoff]
    test = df[df["Authorization Date"] >= cutoff]

    if len(train) == 0 or len(test) == 0:
        continue

    results.append({
        "cutoff": cutoff,
        "train_rows": len(train),
        "test_rows": len(test),
        "train_pct": len(train) / len(df),
        "train_fraud_rate": train["fraud_label"].mean(),
        "test_fraud_rate": test["fraud_label"].mean(),
        "train_fraud_count": train["fraud_label"].sum(),
        "test_fraud_count": test["fraud_label"].sum(),
    })

sweep_df = pd.DataFrame(results)


import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

axes[0].plot(sweep_df["cutoff"], sweep_df["train_pct"] * 100, color="steelblue")
axes[0].axhline(75, color="gray", linestyle="--", alpha=0.5)
axes[0].axhline(80, color="gray", linestyle="--", alpha=0.5)
axes[0].set_ylabel("Train % of total rows")
axes[0].set_title("Train/test size ratio vs. cutoff")

axes[1].plot(sweep_df["cutoff"], sweep_df["train_fraud_rate"] * 100, label="Train fraud rate", color="crimson")
axes[1].plot(sweep_df["cutoff"], sweep_df["test_fraud_rate"] * 100, label="Test fraud rate", color="darkorange")
axes[1].set_ylabel("Fraud rate (%)")
axes[1].set_xlabel("Cutoff date")
axes[1].legend()
axes[1].set_title("Fraud rate in train vs. test at each cutoff")

plt.tight_layout()
plt.show()