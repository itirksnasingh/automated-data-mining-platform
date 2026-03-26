import time
from src.utils.logger import get_logger

logger = get_logger(__name__)


def time_it(func):
    """
    Decorator to measure execution time of functions
    """

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = round(end_time - start_time, 4)

        logger.info(f"{func.__name__} executed in {execution_time} seconds")

        print(f"{func.__name__} executed in {execution_time} seconds")

        return result

    return wrapper