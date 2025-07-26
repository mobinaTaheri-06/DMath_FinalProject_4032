import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os
from ast import literal_eval
from collections import Counter
import pickle

file_path="df_sample.csv"

os.makedirs("output",exist_ok=True) 
df=pd.read_csv(file_path,usecols=["sender_email","all_recipient_emails"])
df=df.dropna(subset=["sender_email","all_recipient_emails"])
df=df.head(100) 
df["all_recipient_emails"] = df["all_recipient_emails"].apply(literal_eval)

edges=[]

for _, row in df.iterrows():
    sender=row["sender_email"].strip().lower()
    for receiver in row["all_recipient_emails"]:
        receiver = receiver.strip().lower()
        edges.append((sender, receiver))
        
edge_weights=Counter(edges)
 
G = nx.DiGraph()
for (u, v), w in edge_weights.items():
    G.add_edge(u, v, weight=w)

 
print("nodes:", G.number_of_nodes())
print("edges:", G.number_of_edges())

 
sub_nodes = list(G.nodes())[:20]
H = G.subgraph(sub_nodes)
plt.figure(figsize=(12, 7))
nx.draw_spring(H, with_labels=True, node_size=1000, node_color='skyblue', arrows=True, font_size=13)
plt.title("Subgragh")
plt.tight_layout()
plt.savefig("output/sample_graph.png", dpi=700, bbox_inches="tight") 
 
with open("output/graph.pkl", "wb") as f:
    pickle.dump(G,f)


    
    
 