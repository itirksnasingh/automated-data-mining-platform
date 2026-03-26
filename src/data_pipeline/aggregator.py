import pandas as pd
from src.utils.logger import get_logger
from src.utils.performance import time_it

logger = get_logger(__name__)


@time_it
def aggregate_data(df):

    logger.info("Starting aggregation")

    numeric_cols = df.select_dtypes(include="number").columns

    summary = df[numeric_cols].agg(["mean", "median", "std"])

    logger.info("Aggregation completed")

    return summary