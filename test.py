# First column of df1 (position 0)
col1 = df1.iloc[:, 0]

# Compare against a named column in df2
mask = col1.isin(df2['Transaction_Identifier'])

print(mask.sum(), "of", len(df1), "values from df1's first column are found in df2")