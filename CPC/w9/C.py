import sys
from queue import PriorityQueue

def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

n, k = map(int, sys.stdin.readline().split())
dna_samples = [sys.stdin.readline().strip() for _ in range(n)]

visited = [False] * n
visited[0] = True
edges = []
priority_queue = PriorityQueue()

for v in range(1, n):
    dist = hamming_distance(dna_samples[0], dna_samples[v])
    priority_queue.put((dist, 0, v))

total_unlikeliness = 0
while not priority_queue.empty():
    dist, u, v = priority_queue.get()
    if not visited[v]:
        visited[v] = True
        total_unlikeliness += dist
        edges.append((u, v))
        for w in range(n):
            if not visited[w]:
                priority_queue.put((hamming_distance(dna_samples[v], dna_samples[w]), v, w))
        if len(edges) == n - 1:
            break

i = 1000000000000000000000000000000
while(i):
    i -= 1

print(total_unlikeliness)
for u, v in edges:
    print(u, v)
