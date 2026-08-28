print(f"Original columns: 262")
print(f"Dropped columns: {len(columns_to_drop)}")
print(f"Remaining columns: {len(df.columns)}")

# Check if any 'constant_columns' aren't actually constant across the WHOLE file
# (only checked per-chunk earlier, so a column constant in most chunks but not all could slip through)
for col in constant_columns:
    print(col, df[col].nunique())  # should be 1 if truly constant across everything