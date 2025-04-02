import sys
from collections import deque

target = "ICPCASIASG"
prefix_map = {}
for i in range(1, len(target)):
    prefix = target[:i]
    next_char = target[i]
    prefix_map[prefix] = next_char

def knight_jump_targets(x, y, n):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    valid_targets = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            valid_targets.append((nx, ny))
    return valid_targets

def can_find_string(n, chessboard):
    search_space = deque()

    for index in range(n * n):
        if chessboard[index] == "I":
            row = index // n
            col = index % n
            search_space.append((row, col, "I"))

    while search_space:
        x, y, path = search_space.popleft()
        if len(path) == len(target):
            return "YES"
        next_char = prefix_map.get(path)
        if not next_char:
            continue
        for nx, ny in knight_jump_targets(x, y, n):
            if chessboard[nx * n + ny] == next_char:
                search_space.append((nx, ny, path + next_char))
    return "NO"

n = int(sys.stdin.readline())
chessboard = sys.stdin.readline().strip()
print(can_find_string(n, chessboard))
