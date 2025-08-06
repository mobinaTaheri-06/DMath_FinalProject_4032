import pandas as pd
import networkx as nx

df = pd.read_csv("sample2.csv")

G = nx.DiGraph()
for _, row in df.iterrows():
    G.add_edge(row['source'], row['target'], weight=row['weight'])

components = list(nx.strongly_connected_components(G))

print(f"connected components: {len(components)}")
for i, comp in enumerate(components, 1):
    print(f"{i}: {comp}")