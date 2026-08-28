import pandas as pd

constant_values = {}
non_constant = set()

for chunk in pd.read_csv(
    "file.csv",
    encoding="cp1252",
    chunksize=100_000
):
    for col in chunk.columns:

        if col in non_constant:
            continue

        values = chunk[col].dropna().unique()

        if len(values) == 0:
            continue

        if col not in constant_values:
            # First non-null value seen
            constant_values[col] = values[0]

        else:
            # Check whether any value differs from the known constant
            if any(value != constant_values[col] for value in values):
                non_constant.add(col)
                constant_values.pop(col, None)


constant_columns = list(constant_values.keys())

print("Constant columns:")
print(constant_columns)

print("\nValues:")
for col in constant_columns:
    print(f"{col} = {constant_values[col]}")