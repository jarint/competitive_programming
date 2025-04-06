import sys


# all-pairs shortest poth problem can be solved with
# Floyd-Warshall algorithm: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/ 

INFTY = 1000000

while True:
    n, m, q = map(int, sys.stdin.readline().split())
    if n == m == q == 0:
        break
    
    # the diagonal is 0's
    dist = [[INFTY] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        dist[u][v] = min(dist[u][v], w)

    # First pass
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < INFTY and dist[k][j] < INFTY:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Second pass
    for k in range(n):
        if dist[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < INFTY and dist[k][j] < INFTY:
                        dist[i][j] = -INFTY

    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if dist[u][v] == INFTY:
            print("Impossible")
        elif dist[u][v] == -INFTY:
            print("-Infinity")
        else:
            print(dist[u][v])
    print()
