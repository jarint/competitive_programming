import sys

def find(a, parent):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
            if rank[root_a] == rank[root_b]:
                rank[root_b] += 1
        return True
    return False

n, m = map(int, sys.stdin.readline().split())
parent = list(range(n))
rank = [0] * n

edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

edges_used = 0
max_edge = 0

for u, v, w in edges:
    if edges_used == n - 1:
        break
    if union(u, v, parent, rank):
        edges_used += 1
        max_edge = w

if edges_used != n - 1:
    print("IMPOSSIBLE")
else:
    print(f"{max_edge}")
