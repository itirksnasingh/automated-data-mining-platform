import pandas as pd
from src.utils.logger import get_logger
from src.utils.performance import time_it

logger = get_logger(__name__)


@time_it
def load_dataset(file):

    logger.info("Loading dataset")

    df = pd.read_csv(file)

    logger.info(f"Dataset loaded: {df.shape}")

    return df