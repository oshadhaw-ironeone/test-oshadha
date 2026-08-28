def clean_id(series):
    return pd.to_numeric(series, errors="coerce").astype("Int64").astype("string").str.strip()


def create_transaction_match_key_confirm_fraud(df):
    cols = [
        "Authorization Identifier",
        "Merchant Name",
        "Transaction Amount"
    ]

    mask = df[cols].notna().all(axis=1)

    df["transaction_match_key"] = pd.NA

    df.loc[mask, "transaction_match_key"] = (
        clean_id(df.loc[mask, "Authorization Identifier"]) + "|" +
        df.loc[mask, "Merchant Name"].astype("string").str.strip() + "|" +
        df.loc[mask, "Transaction Amount"].astype("string").str.strip()
    )
    return df


def create_transaction_match_key_fraud_analysis(df):
    cols = [
        "Authorization Identifier",
        "Merchant Name",
        "Authorization Amount"
    ]

    mask = df[cols].notna().all(axis=1)

    df["transaction_match_key"] = pd.NA

    df.loc[mask, "transaction_match_key"] = (
        clean_id(df.loc[mask, "Authorization Identifier"]) + "|" +
        df.loc[mask, "Merchant Name"].astype("string").str.strip() + "|" +
        df.loc[mask, "Authorization Amount"].astype("string").str.strip()
    )
    return df