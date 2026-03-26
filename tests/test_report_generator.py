import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.intelligence.dataset_intelligence import DatasetIntelligence
from src.intelligence.dataset_quality import DatasetQualityAnalyzer
from src.intelligence.insight_generator import InsightGenerator
from src.mining.pattern_engine import PatternDiscoveryEngine
from src.reporting.report_generator import ReportGenerator

df = pd.read_csv(project_root / "data/raw/online_retail1.csv")

# Intelligence
intelligence = DatasetIntelligence(df)
summary = intelligence.dataset_summary()

# Quality
quality = DatasetQualityAnalyzer(df)
quality_report = quality.generate_quality_report()

# Patterns
engine = PatternDiscoveryEngine(df)

fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

patterns = engine.run(fact_sales_path)

# Insights
insight_engine = InsightGenerator()
insights = insight_engine.generate_all_insights(patterns)

# Report
report = ReportGenerator()

file_path = report.generate_report(summary, quality_report, insights)

print("Report generated:", file_path)