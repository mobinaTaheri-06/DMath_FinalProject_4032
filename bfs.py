import csv
from collections import deque

graph = {}

with open('sample2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        source = row['source']
        target = row['target']
        if source not in graph:
            graph[source] = []
        graph[source].append(target)

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])  

    while queue:
        path = queue.popleft()
        node = path[-1]         

        if node == goal:
            return path  

        if node not in visited:
            visited.add(node)
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None 

start_node = 'Alice'
end_node = 'Charlie'
shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}:")
    print(" → ".join(shortest_path))
else:
    print(f"No path found from {start_node} to {end_node}.")
