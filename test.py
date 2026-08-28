full_dupes = df_y[df_y["Authorization Identifier"].isin(dupes["Authorization Identifier"].unique())]
full_dupes.sort_values("Authorization Identifier")