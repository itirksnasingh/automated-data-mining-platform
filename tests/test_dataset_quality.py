import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.intelligence.dataset_quality import DatasetQualityAnalyzer

df = pd.read_csv(project_root / "data/raw/online_retail1.csv")

quality = DatasetQualityAnalyzer(df)

report = quality.generate_quality_report()

print("Dataset Quality Report")
print("----------------------")

for key, value in report.items():
    print(f"{key}: {value}")