import pandas as pd

from src.intelligence.dataset_intelligence import DatasetIntelligence

from src.mining.customer_clustering import perform_customer_clustering
from src.mining.association_rules import generate_association_rules


class PatternDiscoveryEngine:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.dataset_intelligence = DatasetIntelligence(df)


    # ---------------------------------
    # Run pattern discovery
    # ---------------------------------
    def run(self, fact_sales_path=None):

        dataset_type = self.dataset_intelligence.detect_dataset_type()

        results = {
            "dataset_type": dataset_type,
            "clustering": None,
            "association_rules": None,
            "correlations": None
        }

        # -----------------------------
        # Transaction dataset
        # -----------------------------
        if dataset_type == "Transactional Dataset":

            if fact_sales_path is not None:
                rules = generate_association_rules(fact_sales_path)

                results["association_rules"] = rules

        # -----------------------------
        # Customer dataset
        # -----------------------------
        elif dataset_type == "Customer Dataset":

            if fact_sales_path is not None:
                clusters = perform_customer_clustering(fact_sales_path)

                results["clustering"] = clusters

        # -----------------------------
        # General dataset
        # -----------------------------
        else:

            numeric_df = self.df.select_dtypes(include="number")

            if len(numeric_df.columns) > 1:
                correlations = numeric_df.corr()

                results["correlations"] = correlations

        return results