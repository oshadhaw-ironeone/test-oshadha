columns = pd.read_csv(file_name, encoding="cp1252", nrows=0).columns
print(len(columns))  # 262

for i in range(100, 120):
    col = columns[i]
    print(i, repr(col))
    try:
        df = pd.read_csv(file_name, encoding="cp1252", usecols=[col])
    except Exception as e:
        print(f"  -> FAILED: {e}")