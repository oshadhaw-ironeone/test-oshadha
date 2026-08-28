print(f"Original: 262, Dropped requested: {len(columns_to_drop)}, Expected remaining: {262 - len(columns_to_drop)}")
print(f"Actual df columns: {len(df.columns)}")
print(df.columns.tolist())