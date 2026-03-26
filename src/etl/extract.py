import pandas as pd
from pathlib import Path


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract raw retail dataset from CSV file.
    """

    try:
        df = pd.read_csv(file_path, encoding="utf-8")

        print("Extraction successful")
        print("Dataset shape:", df.shape)

        return df

    except Exception as e:
        print("Error during extraction:", e)
        raise