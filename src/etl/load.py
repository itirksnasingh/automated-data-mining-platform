import pandas as pd
from pathlib import Path


def load_data(df: pd.DataFrame, warehouse_path: Path):

    print("Starting warehouse loading...")

    warehouse_path.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # Customer Dimension
    # -------------------------
    dim_customer = df[["CustomerID", "Country"]].drop_duplicates()

    dim_customer = dim_customer.rename(columns={
        "CustomerID": "customer_id",
        "Country": "location"
    })

    dim_customer.to_csv(warehouse_path / "dim_customer.csv", index=False)

    # -------------------------
    # Product Dimension
    # -------------------------
    dim_product = df[["StockCode", "Description"]].drop_duplicates()

    dim_product = dim_product.rename(columns={
        "StockCode": "product_id",
        "Description": "product_name"
    })

    dim_product.to_csv(warehouse_path / "dim_product.csv", index=False)

    # -------------------------
    # Store Dimension
    # -------------------------
    dim_store = df[["Country"]].drop_duplicates()

    dim_store = dim_store.rename(columns={
        "Country": "region"
    })

    dim_store["store_id"] = range(1, len(dim_store) + 1)

    dim_store.to_csv(warehouse_path / "dim_store.csv", index=False)

    # -------------------------
    # Time Dimension
    # -------------------------
    dim_time = pd.DataFrame()

    dim_time["date"] = df["InvoiceDate"].dt.date
    dim_time = dim_time.drop_duplicates()

    dim_time["day"] = pd.to_datetime(dim_time["date"]).dt.day
    dim_time["month"] = pd.to_datetime(dim_time["date"]).dt.month
    dim_time["quarter"] = pd.to_datetime(dim_time["date"]).dt.quarter
    dim_time["year"] = pd.to_datetime(dim_time["date"]).dt.year

    dim_time.to_csv(warehouse_path / "dim_time.csv", index=False)

    # -------------------------
    # Fact Table
    # -------------------------
    fact_sales = df.copy()

    fact_sales = fact_sales.rename(columns={
        "InvoiceNo": "transaction_id",
        "StockCode": "product_id",
        "CustomerID": "customer_id",
        "Quantity": "quantity",
        "Revenue": "revenue"
    })

    fact_sales["date"] = fact_sales["InvoiceDate"].dt.date

    fact_sales = fact_sales[[
        "transaction_id",
        "product_id",
        "customer_id",
        "quantity",
        "revenue",
        "date",
        "Country"
    ]]

    fact_sales.to_csv(warehouse_path / "fact_sales.csv", index=False)

    print("Warehouse tables created successfully!")