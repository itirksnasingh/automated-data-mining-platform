import pandas as pd


class InsightGenerator:

    def __init__(self):
        pass


    # ---------------------------------
    # Association Rule Insights
    # ---------------------------------
    def generate_association_insights(self, rules_df: pd.DataFrame):

        insights = []

        if rules_df is None or rules_df.empty:
            return insights

        top_rules = rules_df.sort_values("confidence", ascending=False).head(5)

        for _, row in top_rules.iterrows():

            antecedent = list(row["antecedents"])[0]
            consequent = list(row["consequents"])[0]
            confidence = round(row["confidence"] * 100, 2)

            insight = (
                f"Customers who purchase '{antecedent}' also purchase "
                f"'{consequent}' in {confidence}% of transactions."
            )

            insights.append(insight)

        return insights


    # ---------------------------------
    # Cluster Insights
    # ---------------------------------
    def generate_cluster_insights(self, cluster_df: pd.DataFrame):

        insights = []

        if cluster_df is None or cluster_df.empty:
            return insights

        cluster_summary = cluster_df.groupby("cluster")["total_spent"].mean()

        overall_avg = cluster_df["total_spent"].mean()

        for cluster_id, avg_spend in cluster_summary.items():

            if avg_spend > overall_avg * 1.5:

                insights.append(
                    f"Customers in Cluster {cluster_id} spend significantly more "
                    f"than average and represent high-value customers."
                )

            elif avg_spend < overall_avg * 0.5:

                insights.append(
                    f"Cluster {cluster_id} customers spend much less than average, "
                    f"indicating a low-value segment."
                )

        return insights


    # ---------------------------------
    # Correlation Insights
    # ---------------------------------
    def generate_correlation_insights(self, corr_matrix: pd.DataFrame):

        insights = []

        if corr_matrix is None or corr_matrix.empty:
            return insights

        for col in corr_matrix.columns:

            for row in corr_matrix.index:

                if col != row:

                    corr = corr_matrix.loc[row, col]

                    if abs(corr) > 0.7:

                        insights.append(
                            f"Strong relationship detected between '{row}' and '{col}' "
                            f"(correlation: {round(corr,2)})."
                        )

        return insights


    # ---------------------------------
    # Master Insight Generator
    # ---------------------------------
    def generate_all_insights(self, pattern_results):

        insights = []

        if pattern_results["association_rules"] is not None:
            insights += self.generate_association_insights(
                pattern_results["association_rules"]
            )

        if pattern_results["clustering"] is not None:
            insights += self.generate_cluster_insights(
                pattern_results["clustering"]
            )

        if pattern_results["correlations"] is not None:
            insights += self.generate_correlation_insights(
                pattern_results["correlations"]
            )

        return insights