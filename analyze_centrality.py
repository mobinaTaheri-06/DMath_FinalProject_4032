import pickle
import networkx as nx 

with open ("output/graph.pkl","rb") as f:
    G=pickle.load(f)
    
centrality = nx.degree_centrality(G)
most_important_centrality=max(centrality.items(),key=lambda x :x[1])

closeness = nx.closeness_centrality(G)
most_important_closeness=max(closeness.items(),key=lambda x:x[1])

betweenness = nx.betweenness_centrality(G)
most_important_betweenness=max(betweenness.items(),key=lambda x:x[1])

 

print("degree centrality:"+ most_important_centrality[0])
print("closeness centrality:"+most_important_closeness[0])
print("betweenness centrality:"+most_important_betweenness[0])
 
 