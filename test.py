def clean_amount(series):
    return pd.to_numeric(series, errors="coerce").round(2).map(lambda x: f"{x:.2f}" if pd.notna(x) else pd.NA).astype("string")

def create_transaction_match_key_confirm_fraud(df):
    cols = ["Authorization Identifier", "Merchant Name", "Transaction Amount"]
    mask = df[cols].notna().all(axis=1)
    df["transaction_match_key"] = pd.NA
    df.loc[mask, "transaction_match_key"] = (
        clean_id(df.loc[mask, "Authorization Identifier"]) + "|" +
        df.loc[mask, "Merchant Name"].astype("string").str.strip() + "|" +
        clean_amount(df.loc[mask, "Transaction Amount"])
    )
    return df


def create_transaction_match_key_fraud_analysis(df):
    cols = ["Authorization Identifier", "Merchant Name", "Authorization Amount"]
    mask = df[cols].notna().all(axis=1)
    df["transaction_match_key"] = pd.NA
    df.loc[mask, "transaction_match_key"] = (
        clean_id(df.loc[mask, "Authorization Identifier"]) + "|" +
        df.loc[mask, "Merchant Name"].astype("string").str.strip() + "|" +
        clean_amount(df.loc[mask, "Authorization Amount"])
    )
    return df