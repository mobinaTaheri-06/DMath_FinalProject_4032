import pickle

with open("output/graph.pkl", "rb") as f:
    G=pickle.load(f)

   
if G.is_directed():
    print("this gragh is directed.")
    for node in list(G.nodes())[:10]:
        print(f"{node}:\nin_degree:{G.in_degree(node)}\nout_degree:{G.out_degree(node)}")
else:
    print("this gragh is not directed!")
    for node in list(G.nodes())[:10]:
        print(f"{node}:\n degree:{G.degree(node)}")


has_weight=False
for u,v,data in G.edges(data=True):
    if 'weight' in data: 
        has_weight=True
        break

if has_weight:
    print("this gragh is weighted.") 
else:
    print("this gragh is not weighted!") 
      
 