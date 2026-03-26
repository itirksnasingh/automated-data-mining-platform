import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.mining.pattern_engine import PatternDiscoveryEngine
from src.intelligence.insight_generator import InsightGenerator

df = pd.read_csv(project_root / "data/raw/online_retail1.csv")

fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

pattern_engine = PatternDiscoveryEngine(df)

results = pattern_engine.run(fact_sales_path)

insight_engine = InsightGenerator()

insights = insight_engine.generate_all_insights(results)

print("\nGenerated Insights\n")

for insight in insights:
    print("-", insight)