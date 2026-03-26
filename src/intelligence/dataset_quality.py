import pandas as pd
import numpy as np


class DatasetQualityAnalyzer:

    def __init__(self, df: pd.DataFrame):
        self.df = df


    # -----------------------------
    # Basic dataset statistics
    # -----------------------------
    def basic_summary(self):

        summary = {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1],
            "numeric_columns": self.df.select_dtypes(include=np.number).columns.tolist(),
            "categorical_columns": self.df.select_dtypes(include="object").columns.tolist()
        }

        return summary


    # -----------------------------
    # Missing values
    # -----------------------------
    def missing_values(self):

        missing_count = self.df.isnull().sum().sum()

        total_cells = self.df.shape[0] * self.df.shape[1]

        missing_percentage = (missing_count / total_cells) * 100

        return {
            "missing_count": int(missing_count),
            "missing_percentage": round(missing_percentage, 2)
        }


    # -----------------------------
    # Duplicate rows
    # -----------------------------
    def duplicate_rows(self):

        duplicates = self.df.duplicated().sum()

        duplicate_percentage = (duplicates / len(self.df)) * 100

        return {
            "duplicate_rows": int(duplicates),
            "duplicate_percentage": round(duplicate_percentage, 2)
        }


    # -----------------------------
    # Outlier detection
    # -----------------------------
    def detect_outliers(self):

        numeric_df = self.df.select_dtypes(include=np.number)

        outlier_count = 0

        for column in numeric_df.columns:

            Q1 = numeric_df[column].quantile(0.25)
            Q3 = numeric_df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = numeric_df[
                (numeric_df[column] < lower_bound) |
                (numeric_df[column] > upper_bound)
            ]

            outlier_count += len(outliers)

        return {
            "outlier_records": int(outlier_count)
        }


    # -----------------------------
    # Full quality report
    # -----------------------------
    def generate_quality_report(self):

        summary = self.basic_summary()

        missing = self.missing_values()

        duplicates = self.duplicate_rows()

        outliers = self.detect_outliers()

        report = {
            "rows": summary["rows"],
            "columns": summary["columns"],
            "missing_values_percent": missing["missing_percentage"],
            "duplicate_rows_percent": duplicates["duplicate_percentage"],
            "outlier_records": outliers["outlier_records"]
        }

        return report