import sys
import heapq

sys.setrecursionlimit(10000) # we have to go deeper!

n, k = map(int, sys.stdin.readline().strip().split())
adj_list = [[] for _ in range(n)]
in_degree = [0] * n

for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split())
    adj_list[a].append(b)
    in_degree[b] += 1

# Copy of in_degree for second run
in_degree2 = in_degree[:]

# First run - min-heap (lex smallest topological sort)
heap = []
for a in range(n):
    if in_degree[a] == 0:
        heapq.heappush(heap, a)

topo1 = []
while heap:
    a = heapq.heappop(heap)
    topo1.append(a)
    for b in adj_list[a]:
        in_degree[b] -= 1
        if in_degree[b] == 0:
            heapq.heappush(heap, b)

# Second run - max-heap (lex largest topological sort)
heap2 = []
for a in range(n):
    if in_degree2[a] == 0:
        heapq.heappush(heap2, -a)  # max-heap by pushing -a

topo2 = []
while heap2:
    a = -heapq.heappop(heap2)
    topo2.append(a)
    for b in adj_list[a]:
        in_degree2[b] -= 1
        if in_degree2[b] == 0:
            heapq.heappush(heap2, -b)

# Compare both sorts
if topo1 == topo2:
    print(' '.join(map(str, topo1)))
else:
    print("back to the lab")
