import pandas as pd
import plotly.express as px


class ExploratoryAnalysis:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    # ---------------------------------
    # Numeric Columns
    # ---------------------------------
    def get_numeric_columns(self):

        return self.df.select_dtypes(include="number").columns.tolist()

    # ---------------------------------
    # Distribution Plot
    # ---------------------------------
    def distribution_plots(self):

        plots = []

        numeric_cols = self.get_numeric_columns()

        for col in numeric_cols[:4]:

            fig = px.histogram(
                self.df,
                x=col,
                title=f"Distribution of {col}"
            )

            plots.append(fig)

        return plots

    # ---------------------------------
    # Correlation Heatmap
    # ---------------------------------
    def correlation_heatmap(self):

        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            return None

        corr = numeric_df.corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            title="Feature Correlation Heatmap"
        )

        return fig

    # ---------------------------------
    # Scatter Plot Relationships
    # ---------------------------------
    def scatter_plots(self):

        plots = []

        numeric_cols = self.get_numeric_columns()

        if len(numeric_cols) < 2:
            return plots

        x = numeric_cols[0]

        for y in numeric_cols[1:4]:

            fig = px.scatter(
                self.df,
                x=x,
                y=y,
                title=f"{x} vs {y}"
            )

            plots.append(fig)

        return plots