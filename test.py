dupes = df_y[df_y["Authorization Identifier"].duplicated(keep=False) & df_y["Authorization Identifier"].notna()]
print(dupes["Authorization Identifier"].value_counts())