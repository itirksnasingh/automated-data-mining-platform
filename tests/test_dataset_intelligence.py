import sys
from pathlib import Path
import pandas as pd

# Add project root to Python path
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.intelligence.dataset_intelligence import DatasetIntelligence


# Load dataset
df = pd.read_csv(project_root / "data/raw/online_retail1.csv")

engine = DatasetIntelligence(df)

print("Dataset Summary:")
print(engine.dataset_summary())

print("\nDetected Dataset Type:")
print(engine.detect_dataset_type())

print("\nRecommended Analyses:")
print(engine.recommended_analyses())