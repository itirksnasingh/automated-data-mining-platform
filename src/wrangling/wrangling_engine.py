import numpy as np
import pandas as pd
from src.utils.logger import get_logger
from src.utils.performance import time_it

logger = get_logger(__name__)


class DataWranglingEngine:

    def __init__(self, df: pd.DataFrame):

        self.df = df

    # ------------------------------------------------
    # GroupBy Aggregation
    # ------------------------------------------------

    @time_it
    def groupby_summary(self):

        logger.info("Running groupby aggregation")

        numeric_cols = self.df.select_dtypes(include="number").columns

        summary = (
            self.df[numeric_cols]
            .agg(["mean", "median", "std", "min", "max"])
        )

        return summary

    # ------------------------------------------------
    # Pivot Table Analysis
    # ------------------------------------------------

    @time_it
    def pivot_analysis(self):

        logger.info("Generating pivot table")

        numeric_cols = self.df.select_dtypes(include="number").columns
        cat_cols = self.df.select_dtypes(include="object").columns

        if len(cat_cols) == 0 or len(numeric_cols) == 0:
            return None

        pivot = pd.pivot_table(
            self.df,
            values=numeric_cols[0],
            index=cat_cols[0],
            aggfunc="mean"
        )

        return pivot

    # ------------------------------------------------
    # Feature Engineering
    # ------------------------------------------------

    @time_it
    def feature_engineering(self):

        logger.info("Running feature engineering")

        df_copy = self.df.copy()

        numeric_cols = df_copy.select_dtypes(include="number").columns

        for col in numeric_cols:

            df_copy[f"{col}_log"] = df_copy[col].apply(
                lambda x: 0 if x <= 0 else np.log1p(x)
            )

        return df_copy.head()

    # ------------------------------------------------
    # Data Reshaping Example
    # ------------------------------------------------

    @time_it
    def reshape_data(self):

        logger.info("Running data reshaping")

        reshaped = self.df.melt()

        return reshaped.head()