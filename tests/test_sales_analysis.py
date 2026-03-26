import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.analytics.sales_analysis import (
    load_sales_data,
    monthly_revenue_analysis,
    top_products_analysis,
    country_sales_analysis
)

fact_sales_path = project_root / "data" / "warehouse" / "fact_sales.csv"

df = load_sales_data(fact_sales_path)

monthly_sales, fig1 = monthly_revenue_analysis(df)
top_products, fig2 = top_products_analysis(df)
country_sales, fig3 = country_sales_analysis(df)

print(monthly_sales.head())
print(top_products.head())
print(country_sales.head())