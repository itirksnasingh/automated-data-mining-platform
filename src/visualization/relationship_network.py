import networkx as nx
import plotly.graph_objects as go


class RelationshipNetwork:

    def __init__(self, rules_df):
        self.rules_df = rules_df

    # ---------------------------------
    # Build Network Graph
    # ---------------------------------
    def build_graph(self):

        G = nx.Graph()

        if self.rules_df is None or self.rules_df.empty:
            return G

        top_rules = self.rules_df.sort_values(
            "confidence", ascending=False
        ).head(20)

        for _, row in top_rules.iterrows():

            antecedent = list(row["antecedents"])[0]
            consequent = list(row["consequents"])[0]

            confidence = row["confidence"]

            G.add_edge(antecedent, consequent, weight=confidence)

        return G

    # ---------------------------------
    # Plot Network Graph
    # ---------------------------------
    def plot_graph(self):

        G = self.build_graph()

        pos = nx.spring_layout(G, seed=42)

        edge_x = []
        edge_y = []

        for edge in G.edges():

            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]

            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)

            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=1),
            hoverinfo='none',
            mode='lines'
        )

        node_x = []
        node_y = []

        for node in G.nodes():

            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode='markers+text',
            text=list(G.nodes()),
            textposition="top center",
            marker=dict(
                size=12
            )
        )

        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title="Product Relationship Network",
                showlegend=False,
                hovermode='closest'
            )
        )

        return fig