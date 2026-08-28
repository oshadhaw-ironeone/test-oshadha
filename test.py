raw_header = pd.read_csv(file_name, encoding="cp1252", nrows=0, header=None).iloc[0].tolist()
print(len(raw_header))  # should be 262

import collections
counts = collections.Counter(raw_header)
dupes = {name: n for name, n in counts.items() if n > 1}
print(f"{len(dupes)} duplicate name(s) found:")
for name, n in dupes.items():
    positions = [i for i, c in enumerate(raw_header) if c == name]
    print(f"  {name!r} appears {n}x at positions {positions}")