from src.utils.logger import get_logger
from src.utils.performance import time_it

logger = get_logger(__name__)


@time_it
def clean_data(df):

    logger.info("Starting data cleaning")

    df = df.drop_duplicates()

    df = df.fillna(method="ffill")

    logger.info("Data cleaning completed")

    return df