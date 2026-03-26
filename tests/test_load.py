import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data


file_path = project_root / "data" / "raw" / "online_retail1.csv"
warehouse_path = project_root / "data" / "warehouse"

df = extract_data(file_path)
df_clean = transform_data(df)

load_data(df_clean, warehouse_path)

print("Warehouse built successfully.")