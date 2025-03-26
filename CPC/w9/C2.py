import sys

def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

n, k = map(int, sys.stdin.readline().split())
dna_samples = [sys.stdin.readline().strip() for _ in range(n)]

infty = float('inf')

visited = [False] * n
distances = [infty] * n
parent = [-1] * n

distances[0] = 0
total_unlikeliness = 0
edges = []

for _ in range(n):
    # look for unvisited node with smallest distance
    min_dist = float('inf')
    u = -1
    for i in range(n):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            u = i

    visited[u] = True
    total_unlikeliness += min_dist

    if parent[u] != -1:
        edges.append((parent[u], u))

    # update distances from this node
    for v in range(n):
        if not visited[v]:
            dist = hamming_distance(dna_samples[u], dna_samples[v])
            if dist < distances[v]:
                distances[v] = dist
                parent[v] = u
    



print(total_unlikeliness)
for u, v in edges:
    print(u, v)
