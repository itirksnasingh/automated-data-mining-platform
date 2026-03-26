import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.mining.association_rules import generate_association_rules
from src.visualization.relationship_network import RelationshipNetwork

fact_sales_path = project_root / "data/warehouse/fact_sales.csv"

rules = generate_association_rules(fact_sales_path)

network = RelationshipNetwork(rules)

fig = network.plot_graph()

fig.show()