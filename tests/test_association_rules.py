import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.mining.association_rules import generate_association_rules


fact_sales_path = project_root / "data" / "warehouse" / "fact_sales.csv"

rules = generate_association_rules(fact_sales_path)

print(rules.head())