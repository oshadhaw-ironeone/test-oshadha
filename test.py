import pandas as pd

constant_values = {}

for chunk in pd.read_csv(
    "file.csv",
    encoding="cp1252",
    chunksize=100_000
):
    for col in chunk.columns:
        values = chunk[col].dropna().unique()

        if col not in constant_values:
            # First non-null value we've seen
            constant_values[col] = values[0] if len(values) else None

        elif len(values) > 0:
            # If a different value appears, it's not constant
            if any(value != constant_values[col] for value in values):
                constant_values[col] = False

constant_columns = [
    col for col, value in constant_values.items()
    if value is not None and value is not False
]

print("Constant columns:")
print(constant_columns)

print("\nValues:")
for col in constant_columns:
    print(col, "=", constant_values[col])