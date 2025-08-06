import csv

graph = {}

with open('sample2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        source = row['source']
        target = row['target']
        if source not in graph:
            graph[source] = []
        graph[source].append(target)

def dfs_cycle_detection(node, graph, visited, rec_stack, path, cycles):
    visited.add(node)
    rec_stack.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_cycle_detection(neighbor, graph, visited, rec_stack, path, cycles)
        elif neighbor in rec_stack:
            cycle_start = path.index(neighbor)
            cycle = path[cycle_start:] + [neighbor]
            cycles.append(cycle)

    rec_stack.remove(node)
    path.pop()

def find_cycles(graph):
    visited = set()
    rec_stack = set()
    cycles = []

    for node in graph:
        if node not in visited:
            dfs_cycle_detection(node, graph, visited, rec_stack, [], cycles)

    return cycles


found_cycles = find_cycles(graph)


if found_cycles:
    print("✅ found --> DFS:")
    for cycle in found_cycles:
        print(" → ".join(cycle))
else:
    print("❌not found")