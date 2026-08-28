common_sentinels = [0, -1, 9999, 99999, 999999, -9999, -99999]

for val in common_sentinels:
    count = (df['column'] == val).sum()
    if count > 0:
        pct = count / len(df) * 100
        print(f"{val}: {count} occurrences ({pct:.1f}%)")