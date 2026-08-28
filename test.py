import pandas as pd
import collections

file_name = "your_file.csv"
chunksize = 100_000

# --- Get raw header (for reference/traceability) ---
raw_header = pd.read_csv(file_name, encoding="cp1252", nrows=1, header=None).iloc[0].tolist()
print(f"Raw header columns: {len(raw_header)}")

# --- Chunked scan ---
null_counts = None
nunique_trackers = None
total_rows = 0
first = True
mangled_columns = None

reader = pd.read_csv(
    file_name,
    encoding="cp1252",
    chunksize=chunksize,
    low_memory=False,
    on_bad_lines="warn",   # switch to "skip" once you've confirmed bad-line volume is fine
)

for chunk_num, chunk in enumerate(reader):
    total_rows += len(chunk)

    if first:
        mangled_columns = chunk.columns.tolist()
        if len(mangled_columns) != len(raw_header):
            print(f"Warning: loaded {len(mangled_columns)} columns but raw header has {len(raw_header)}")
        null_counts = chunk.isna().sum()
        nunique_trackers = {col: set(chunk[col].dropna().unique()) for col in chunk.columns}
        first = False
    else:
        null_counts += chunk.isna().sum()
        for col in chunk.columns:
            if len(nunique_trackers[col]) <= 1:  # stop tracking once confirmed non-constant
                nunique_trackers[col].update(chunk[col].dropna().unique())

    if chunk_num % 10 == 0:
        print(f"Processed {total_rows:,} rows so far...")

print(f"\nTotal rows loaded: {total_rows:,}")

# --- Results ---
all_null_columns = null_counts[null_counts == total_rows].index.tolist()
constant_columns = [
    col for col, vals in nunique_trackers.items()
    if len(vals) == 1 and null_counts[col] == 0
]

print("\nAll null columns:")
print(all_null_columns)

print("\nConstant columns:")
print(constant_columns)