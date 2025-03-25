import sys
input = sys.stdin.readline

def find(a, parent):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b, parent, size):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]

n, q = map(int, input().split())
parent = list(range(n))
size = [1] * n

for _ in range(q):
    line = input().split()
    op, a, b = line[0], int(line[1]), int(line[2])
    if op == "?":
        print("yes" if find(a, parent) == find(b, parent) else "no")
    elif op == "=":
        union(a, b, parent, size)

# this can't literally be just union find...right?
