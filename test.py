for col1 in df_y.columns:
    values_to_check = df_y[col1].to_list()
    for col2 in df.columns:
        mask = df[col2].isin(values_to_check)
        if mask.sum() > 0:
            # check one-to-one: merge matching values and see if mapping is unique both ways
            merged = df_y[[col1]].merge(df[[col2]], left_on=col1, right_on=col2, how='inner')
            forward_unique = merged.groupby(col1)[col2].nunique().max() == 1
            backward_unique = merged.groupby(col2)[col1].nunique().max() == 1
            if forward_unique and backward_unique:
                print(f"{col1} from df_y match {col2} from df and count is {mask.sum()} - ONE-TO-ONE")