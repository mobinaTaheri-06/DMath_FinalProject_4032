import pandas as pd
import heapq
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import pickle

with open ("output/graph.pkl","rb") as f:
    G=pickle.load(f)

def dijkstra(G, start):
    distances = {node: float('inf') for node in G.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor in G.neighbors(current_node):
            weight = G[current_node][neighbor].get('weight', 1)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

start_node = list(G.nodes)[0]
print(f"START NODE :  {start_node}")

shortest_paths = dijkstra(G, start_node)

print("\n📍ALL THE SHORTEST PATH :")
for target_node, distance in shortest_paths.items():
    if target_node != start_node:
        print(f"START NODE : '{start_node}' END NODE :'{target_node}': {distance}")