mapping_check = (
    df.groupby("name")["identifier"]
      .nunique()
      .reset_index(name="identifier_count")
)

mismatches = mapping_check[mapping_check["identifier_count"] > 1]

print(len(mismatches))