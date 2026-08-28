import csv

with open(file_name, encoding="cp1252", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    header_fields = len(header)
    print(f"Header field count: {header_fields}")

    bad_lines = []
    for i, row in enumerate(reader, start=2):
        if len(row) != header_fields:
            bad_lines.append((i, len(row)))
        if i % 500_000 == 0:
            print(f"Checked {i:,} lines so far... ({len(bad_lines)} bad so far)")

print(f"\nTotal ragged lines: {len(bad_lines)}")
print("First 10 ragged lines (line_num, field_count):")
print(bad_lines[:10])