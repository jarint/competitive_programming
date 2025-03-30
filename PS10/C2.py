import sys

def neighbors(i, j, rows, cols, grid, visited):
    for di, dj in [(1, 0), (1, 1), (0, 1), (-1, 1),
                   (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        ni, nj = i + di, j + dj
        if (0 <= ni < rows and
            0 <= nj < cols and
            grid[ni][nj] and
            (ni, nj) not in visited):
            yield ni, nj

def dfs(i, j, rows, cols, grid, visited):
    stack = [(i, j)]
    while stack:
        ci, cj = stack.pop()
        if (ci, cj) in visited:
            continue
        visited.add((ci, cj))
        for ni, nj in neighbors(ci, cj, rows, cols, grid, visited):
            stack.append((ni, nj))

def flood_fill(rows, cols, grid):
    visited = set()
    loops = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) in visited or not grid[i][j]:
                continue
            loops += 1
            dfs(i, j, rows, cols, grid, visited)
    return loops

m, n = map(int, sys.stdin.readline().split())
grid = [[c == '#' for c in sys.stdin.readline().strip()] for _ in range(m)]
print(flood_fill(m, n, grid))
