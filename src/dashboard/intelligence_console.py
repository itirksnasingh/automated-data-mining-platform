import streamlit as st
import pandas as pd
from pathlib import Path
import sys
from streamlit_option_menu import option_menu

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

# existing modules
from src.intelligence.dataset_intelligence import DatasetIntelligence
from src.intelligence.dataset_quality import DatasetQualityAnalyzer
from src.intelligence.insight_generator import InsightGenerator
from src.mining.pattern_engine import PatternDiscoveryEngine
from src.visualization.relationship_network import RelationshipNetwork
from src.reporting.report_generator import ReportGenerator
from src.analytics.exploratory_analysis import ExploratoryAnalysis

# new modules
from src.wrangling.wrangling_engine import DataWranglingEngine


# --------------------------------------------------
# Dataset Type Detector
# --------------------------------------------------

class DatasetTypeDetector:

    def __init__(self, df):
        self.columns = [c.lower() for c in df.columns]

    def detect(self):

        loan_keywords = ["loan", "credit", "income", "applicant", "approval"]
        if sum(any(k in col for k in loan_keywords) for col in self.columns) >= 2:
            return "Loan Dataset"

        student_keywords = ["score", "math", "reading", "writing", "grade"]
        if sum(any(k in col for k in student_keywords) for col in self.columns) >= 2:
            return "Student Dataset"

        house_keywords = ["price", "area", "bedroom", "bathroom", "sqft"]
        if sum(any(k in col for k in house_keywords) for col in self.columns) >= 2:
            return "House Dataset"

        retail_keywords = ["invoice", "product", "stock", "transaction", "quantity"]
        if sum(any(k in col for k in retail_keywords) for col in self.columns) >= 2:
            return "Retail Dataset"

        return "General Dataset"


# --------------------------------------------------
# Page Setup
# --------------------------------------------------

st.set_page_config(
    page_title="Automated Data Mining Platform",
    layout="wide"
)

st.title("Automated Data Mining & Insight Platform")

st.markdown(
"""
Upload any dataset and automatically discover patterns,
generate insights and provide recommendations.
"""
)


# --------------------------------------------------
# Upload Dataset
# --------------------------------------------------

uploaded_file = st.file_uploader("Upload Dataset", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    detector = DatasetTypeDetector(df)
    dataset_type = detector.detect()

    intelligence = DatasetIntelligence(df)

    quality = DatasetQualityAnalyzer(df)
    quality_report = quality.generate_quality_report()

    # --------------------------------------------------
    # KPI Cards
    # --------------------------------------------------

    rows = df.shape[0]
    cols = df.shape[1]
    missing = quality_report["missing_values_percent"]

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Rows", rows)
    k2.metric("Columns", cols)
    k3.metric("Dataset Type", dataset_type)
    k4.metric("Missing %", missing)

    st.divider()

    # --------------------------------------------------
    # Navigation Menu
    # --------------------------------------------------

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Dataset Intelligence",
            "Data Quality",
            "Exploratory Analysis",
            "Data Wrangling",
            "Pattern Discovery",
            "Insights & Recommendations",
            "Relationship Graph",
            "Export Report"
        ]
    )


# --------------------------------------------------
# Dataset Intelligence
# --------------------------------------------------

    if selected == "Dataset Intelligence":

        st.header("Dataset Intelligence")

        summary = intelligence.dataset_summary()

        col1, col2 = st.columns(2)

        col1.metric("Rows", summary["rows"])
        col2.metric("Columns", summary["columns"])

        st.subheader("Recommended Analyses")

        analyses = intelligence.recommended_analyses()

        for a in analyses:
            st.write("✓", a)


# --------------------------------------------------
# Data Quality
# --------------------------------------------------

    elif selected == "Data Quality":

        st.header("Dataset Quality Report")

        col1, col2 = st.columns(2)

        col1.metric("Rows", quality_report["rows"])
        col1.metric("Columns", quality_report["columns"])

        col2.metric("Missing %", quality_report["missing_values_percent"])
        col2.metric("Duplicate %", quality_report["duplicate_rows_percent"])

        st.write("Outliers detected:", quality_report["outlier_records"])


# --------------------------------------------------
# Exploratory Analysis
# --------------------------------------------------

    elif selected == "Exploratory Analysis":

        st.header("Exploratory Data Analysis")

        explorer = ExploratoryAnalysis(df)

        st.info(f"Detected Dataset Type: {dataset_type}")

        st.subheader("Feature Distributions")

        for fig in explorer.distribution_plots():
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Correlation Heatmap")

        heatmap = explorer.correlation_heatmap()

        if heatmap is not None:
            st.plotly_chart(heatmap, use_container_width=True)

        st.subheader("Feature Relationships")

        for fig in explorer.scatter_plots():
            st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# Data Wrangling Engine
# --------------------------------------------------

    elif selected == "Data Wrangling":

        st.header("Data Wrangling Engine")

        wrangler = DataWranglingEngine(df)

        st.subheader("Aggregated Statistics")

        summary = wrangler.groupby_summary()

        st.dataframe(summary)

        st.subheader("Pivot Table Analysis")

        pivot = wrangler.pivot_analysis()

        if pivot is not None:
            st.dataframe(pivot)
        else:
            st.info("No suitable columns for pivot table.")

        st.subheader("Feature Engineering Preview")

        engineered = wrangler.feature_engineering()

        st.dataframe(engineered)

        st.subheader("Data Reshaping Example")

        reshaped = wrangler.reshape_data()

        st.dataframe(reshaped)


# --------------------------------------------------
# Pattern Discovery
# --------------------------------------------------

    elif selected == "Pattern Discovery":

        st.header("Pattern Discovery")

        fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

        engine = PatternDiscoveryEngine(df)
        results = engine.run(fact_sales_path)

        if results["association_rules"] is not None and not results["association_rules"].empty:

            st.subheader("Association Rules")

            st.dataframe(results["association_rules"].head())

        if results["clustering"] is not None:

            st.subheader("Cluster Results")

            st.dataframe(results["clustering"].head())

        if results["correlations"] is not None:

            st.subheader("Correlation Matrix")

            st.dataframe(results["correlations"])


# --------------------------------------------------
# Insights & Recommendations
# --------------------------------------------------

    elif selected == "Insights & Recommendations":

        st.header("Generated Insights")

        fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

        engine = PatternDiscoveryEngine(df)
        patterns = engine.run(fact_sales_path)

        insight_engine = InsightGenerator()

        insights = insight_engine.generate_all_insights(patterns)

        if insights:

            for insight in insights:
                st.success(insight)

        else:

            numeric_df = df.select_dtypes(include="number")

            if numeric_df.shape[1] > 1:

                corr = numeric_df.corr()

                strong_corr = corr.abs().unstack().sort_values(ascending=False)

                strong_corr = strong_corr[strong_corr < 1]

                top_pair = strong_corr.index[0]

                st.success(
                    f"Strong relationship detected between "
                    f"{top_pair[0]} and {top_pair[1]}"
                )

        st.header("Business Recommendations")

        st.info(
            "Use detected patterns and correlations to guide "
            "strategic decisions and predictive modeling."
        )


# --------------------------------------------------
# Relationship Graph
# --------------------------------------------------

    elif selected == "Relationship Graph":

        st.header("Relationship Network")

        fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

        engine = PatternDiscoveryEngine(df)
        results = engine.run(fact_sales_path)

        rules = results["association_rules"]

        if rules is not None and not rules.empty:

            network = RelationshipNetwork(rules)

            fig = network.plot_graph()

            st.plotly_chart(fig, use_container_width=True)

        else:

            st.warning("No association rules found. Showing correlation relationships instead.")

            numeric_df = df.select_dtypes(include="number")

            if numeric_df.shape[1] > 1:

                corr = numeric_df.corr()

                st.subheader("Feature Relationship Matrix")

                st.dataframe(corr)

            else:

                st.info("Not enough numeric columns for relationship analysis.")


# --------------------------------------------------
# Export Report
# --------------------------------------------------

    elif selected == "Export Report":

        st.header("Export Analytics Report")

        summary = intelligence.dataset_summary()

        fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

        engine = PatternDiscoveryEngine(df)
        patterns = engine.run(fact_sales_path)

        insight_engine = InsightGenerator()
        insights = insight_engine.generate_all_insights(patterns)

        report = ReportGenerator()

        file_path = report.generate_report(
            summary,
            quality_report,
            insights
        )

        with open(file_path, "rb") as file:

            st.download_button(
                label="Download Analytics Report",
                data=file,
                file_name="analytics_report.pdf"
            )