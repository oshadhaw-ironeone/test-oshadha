import matplotlib.pyplot as plt
import pandas as pd

df["date"] = pd.to_datetime(df["date"])

# Percentile dates
p20 = df["date"].quantile(0.20)
p50 = df["date"].quantile(0.50)
p80 = df["date"].quantile(0.80)

plt.figure(figsize=(12, 5))

plt.hist(df["date"], bins=30)

plt.axvline(p20, linestyle="--", label=f"20%: {p20.date()}")
plt.axvline(p50, linestyle="--", label=f"50%: {p50.date()}")
plt.axvline(p80, linestyle="--", label=f"80%: {p80.date()}")

plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Date Distribution with Percentile Cutoffs")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()