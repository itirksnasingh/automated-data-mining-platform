import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    print("Starting transformation...")

    # Standardize column names
    df = df.rename(columns={
        "Invoice": "InvoiceNo",
        "Price": "UnitPrice",
        "Customer ID": "CustomerID"
    })

    # Remove rows with missing CustomerID
    df = df.dropna(subset=["CustomerID"])

    # Remove cancelled invoices
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

    # Remove negative quantities
    df = df[df["Quantity"] > 0]

    # Convert date column
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True)

    # Create revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Convert customer id
    df["CustomerID"] = df["CustomerID"].astype(int)

    print("Transformation completed")
    print("Clean dataset shape:", df.shape)

    return df