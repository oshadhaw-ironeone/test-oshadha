dup_ids = dupes["Authorization Identifier"].unique()

for id_val in dup_ids:
    rows = df_y[df_y["Authorization Identifier"] == id_val]
    print(f"\n=== Authorization Identifier: {id_val} ===")
    
    if len(rows) == 2:
        row1, row2 = rows.iloc[0], rows.iloc[1]
        # Compare column by column
        diff_cols = [col for col in df_y.columns if row1[col] != row2[col] and not (pd.isna(row1[col]) and pd.isna(row2[col]))]
        
        if diff_cols:
            print("Changing columns:")
            print(rows[diff_cols])
        else:
            print("Rows are fully identical (true duplicate)")
    else:
        print(f"Found {len(rows)} rows (expected 2) — inspect manually")