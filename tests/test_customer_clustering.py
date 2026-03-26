import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.mining.customer_clustering import perform_customer_clustering


fact_sales_path = project_root / "data" / "warehouse" / "fact_sales.csv"

clusters = perform_customer_clustering(fact_sales_path)

print(clusters.head())
print("\nCluster distribution:")
print(clusters["cluster"].value_counts())