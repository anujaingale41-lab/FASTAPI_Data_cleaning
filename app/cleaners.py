import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # 2. Remove duplicates
    df = df.drop_duplicates()

    # 3. Clean product names
    df["product"] = df["product"].astype(str).str.strip().str.title()

    # 4. Convert quantity to int
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # 5. Convert price to float
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # 6. Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # 7. Drop rows with invalid or missing values
    df = df.dropna(subset=["product", "quantity", "price", "order_date"])

    return df
