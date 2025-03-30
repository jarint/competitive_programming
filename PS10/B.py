import sys

def find_components(graph):
    component_labels = {}
    group_id = 0
    for node in graph:
        if node not in component_labels:
            stack = [node]
            component_labels[node] = group_id
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in component_labels:
                        stack.append(neighbor)
                        component_labels[neighbor] = group_id
            group_id += 1
    return component_labels, group_id

def add_edge(adj, u, v):
    if u not in adj:
        adj[u] = {}
    adj[u][v] = True
    if v not in adj:
        adj[v] = {}
    adj[v][u] = True

n, m, k = map(int, sys.stdin.readline().strip().split())
blue_graph = {}
red_edges = []

for _ in range(m):
    color, u, v = sys.stdin.readline().strip().split()
    u, v = int(u), int(v)
    if color == 'B':
        add_edge(blue_graph, u, v)
    else:
        red_edges.append((u, v))

component_labels, num_components = find_components(blue_graph)
max_blue_edges = len(blue_graph) - num_components


if max_blue_edges < k or len(red_edges) + k < n - 1:
    print(0)
else:
    print(1)
