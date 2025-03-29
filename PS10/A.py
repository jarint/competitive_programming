import sys

def find(a, parent):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b, parent, size):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a == root_b:
        return False
    if size[root_b] > size[root_a]:
        root_a, root_b = root_b, root_a
    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True

def kruskals(n, edges):
    parent = list(range(n))
    size = [1] * n
    clusters = n
    edges.sort()
    total_weight = 0
    i = 0
    while clusters > 1 and i < len(edges):
        w, u, v = edges[i]
        i += 1
        if union(u, v, parent, size):
            total_weight += w
            clusters -= 1
    return total_weight

t = int(sys.stdin.readline().strip())
for _ in range(t):
    m, c = map(int, sys.stdin.readline().strip().split())
    edge_list = []
    for _ in range((c * (c - 1)) // 2):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        edge_list.append((w, u, v))
    mst_weight = kruskals(c, edge_list)
    print("yes" if mst_weight + c <= m else "no")
