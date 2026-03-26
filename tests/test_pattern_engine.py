import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.mining.pattern_engine import PatternDiscoveryEngine

df = pd.read_csv(project_root / "data/raw/online_retail1.csv")

engine = PatternDiscoveryEngine(df)

fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

results = engine.run(fact_sales_path)

print("Dataset Type:", results["dataset_type"])

if results["association_rules"] is not None:
    print("\nAssociation Rules Found:")
    print(results["association_rules"].head())

if results["clustering"] is not None:
    print("\nCluster Results:")
    print(results["clustering"].head())

if results["correlations"] is not None:
    print("\nCorrelation Matrix:")
    print(results["correlations"])