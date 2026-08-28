def create_transaction_match_key(df):
    cols = [
        "Authorization Identifier",
        "Merchant Name",
        "Transaction Amount"
    ]

    mask = df[cols].notna().all(axis=1)

    df["transaction_match_key"] = pd.NA

    df.loc[mask, "transaction_match_key"] = (
        df.loc[mask, "Authorization Identifier"].astype("string").str.strip() + "|" +
        df.loc[mask, "Merchant Name"].astype("string").str.strip() + "|" +
        df.loc[mask, "Transaction Amount"].astype("string").str.strip()
    )