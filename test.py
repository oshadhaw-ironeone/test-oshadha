import re

# Extract everything before the '*' (if present), otherwise keep full name
matched['Merchant_Name_confirmed_clean'] = (
    matched['Merchant Name_confirmed']
    .astype(str)
    .str.split('*').str[0]
    .str.strip()
)

# Check unique values
unique_clean_names = matched['Merchant_Name_confirmed_clean'].unique()
print(f"Unique cleaned Merchant Name_confirmed values: {len(unique_clean_names)}")

with pd.option_context("display.max_rows", 200):
    display(pd.Series(unique_clean_names).sort_values().reset_index(drop=True))