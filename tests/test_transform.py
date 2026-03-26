import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.etl.extract import extract_data
from src.etl.transform import transform_data


file_path = project_root / "data" / "raw" / "online_retail1.csv"

df = extract_data(file_path)

print("Columns:", df.columns)

df_clean = transform_data(df)

print(df_clean.head())