import pandas as pd


class DatasetIntelligence:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    # ---------------------------------
    # Dataset Summary
    # ---------------------------------
    def dataset_summary(self):

        summary = {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1],
            "numeric_columns": self.df.select_dtypes(include=["number"]).columns.tolist(),
            "categorical_columns": self.df.select_dtypes(include=["object"]).columns.tolist()
        }

        return summary

    # ---------------------------------
    # Dataset Type Detection
    # ---------------------------------
    def detect_dataset_type(self):

        columns = [c.lower() for c in self.df.columns]

        # Transaction dataset indicators
        transaction_keywords = [
            "invoice",
            "stock",
            "product",
            "item",
            "order",
            "transaction"
        ]

        for keyword in transaction_keywords:
            for col in columns:
                if keyword in col:
                    return "Transactional Dataset"

        # Customer dataset indicators
        for col in columns:
            if "customer" in col:
                return "Customer Dataset"

        # Time-series dataset detection
        datetime_cols = self.df.select_dtypes(include=["datetime64"]).columns

        if len(datetime_cols) > 0:
            return "Time-Series Dataset"

        return "General Dataset"

    # ---------------------------------
    # Recommended Analyses
    # ---------------------------------
    def recommended_analyses(self):

        dataset_type = self.detect_dataset_type()

        if dataset_type == "Transactional Dataset":

            return [
                "Association Rule Mining",
                "Product Relationship Network",
                "Statistical Analysis"
            ]

        elif dataset_type == "Customer Dataset":

            return [
                "Customer Clustering",
                "Customer Segmentation Insights",
                "Statistical Analysis"
            ]

        elif dataset_type == "Time-Series Dataset":

            return [
                "Trend Analysis",
                "Seasonality Detection",
                "Statistical Analysis"
            ]

        else:

            return [
                "Clustering",
                "Correlation Analysis",
                "Statistical Exploration"
            ]