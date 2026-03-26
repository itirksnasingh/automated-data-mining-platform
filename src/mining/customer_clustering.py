from src.utils.performance import time_it
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


@time_it
def perform_customer_clustering(fact_sales_path):

    print("Loading fact sales...")
    df = pd.read_csv(fact_sales_path)

    # -------------------------
    # Create customer features
    # -------------------------
    customer_features = df.groupby("customer_id").agg(
        total_spent=("revenue", "sum"),
        total_orders=("transaction_id", "nunique"),
        total_items=("quantity", "sum")
    ).reset_index()

    # Average order value
    customer_features["avg_order_value"] = (
        customer_features["total_spent"] /
        customer_features["total_orders"]
    )

    print("Customer feature dataset shape:", customer_features.shape)

    # -------------------------
    # Log transformation
    # -------------------------
    customer_features["log_spent"] = np.log1p(customer_features["total_spent"])
    customer_features["log_items"] = np.log1p(customer_features["total_items"])

    # -------------------------
    # Select clustering features
    # -------------------------
    features = customer_features[
        ["log_spent", "total_orders", "log_items", "avg_order_value"]
    ]

    # -------------------------
    # Feature scaling
    # -------------------------
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # -------------------------
    # K-Means clustering
    # -------------------------
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

    customer_features["cluster"] = kmeans.fit_predict(scaled_features)

    print("Clustering completed")

    return customer_features