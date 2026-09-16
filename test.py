# Make sure the date column is datetime
df_all["Authorization Date"] = pd.to_datetime(df_all["Authorization Date"], errors="coerce")

# Filter to fraud cases only
fraud_df = df_all[df_all["fraud_label"] == 1]  # adjust if label is not 0/1

plt.figure(figsize=(12, 5))
sns.histplot(
    data=fraud_df,
    x="Authorization Date",
    bins=50,          # increase/decrease depending on your date range
    color="crimson"
)
plt.title("Fraud Count Over Time")
plt.xlabel("Authorization Date")
plt.ylabel("Fraud Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()