import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


def generate_association_rules(fact_sales_path):

    print("Loading fact sales...")
    df = pd.read_csv(fact_sales_path)

    # -------------------------
    # Remove very rare products
    # -------------------------
    product_counts = df["product_id"].value_counts()

    frequent_products = product_counts[product_counts > 100].index

    df = df[df["product_id"].isin(frequent_products)]

    print("Products after filtering:", len(frequent_products))

    # -------------------------
    # Basket dataset
    # -------------------------
    basket = (
        df.groupby(["transaction_id", "product_id"])["quantity"]
        .sum()
        .unstack()
        .fillna(0)
    )

    # Convert to boolean matrix
    basket = basket > 0

    print("Basket matrix shape:", basket.shape)

    # -------------------------
    # Apriori
    # -------------------------
    frequent_items = apriori(
        basket,
        min_support=0.02,
        use_colnames=True
    )

    print("Frequent itemsets found:", len(frequent_items))

    # -------------------------
    # Rules
    # -------------------------
    rules = association_rules(
        frequent_items,
        metric="lift",
        min_threshold=1
    )

    rules = rules.sort_values("lift", ascending=False)

    return rules