import sys
from collections import deque

def bfs(rows, cols, grid):
    queue = deque()
    visited = set()

    queue.append((0, 0, 0))
    visited.add((0, 0))

    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return steps

        k = grid[r][c]
        for dr, dc in [(-k, 0), (k, 0), (0, -k), (0, k)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))

    return -1

rows, cols = map(int, sys.stdin.readline().split())
grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(rows)]
print(bfs(rows, cols, grid))
