columns = pd.read_csv(file_name, encoding="cp1252", nrows=0).columns
print(len(columns))

all_null_columns = []
constant_columns = []
failed_columns = []

for i, col in enumerate(columns):
    if i % 20 == 0:
        print(f"{i}/{len(columns)}")
    try:
        df = pd.read_csv(
            file_name,
            encoding="cp1252",
            usecols=[i],
            on_bad_lines="skip",   # skip ragged/malformed rows instead of erroring
            low_memory=False
        )
        if df.shape[1] == 0:
            failed_columns.append((i, col, "empty result"))
            continue
        if df.iloc[:, 0].isna().all():
            all_null_columns.append(col)
        elif df.iloc[:, 0].notna().all() and df.iloc[:, 0].nunique() == 1:
            constant_columns.append(col)
        del df
    except Exception as e:
        failed_columns.append((i, col, str(e)))

print("All null columns:")
print(all_null_columns)
print("\nConstant columns:")
print(constant_columns)
print("\nFailed columns:")
print(failed_columns)