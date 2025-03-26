import math
import sys

start = list(map(float, sys.stdin.readline().split()))
end = list(map(float, sys.stdin.readline().split()))
n = int(sys.stdin.readline()) + 2

points = [start]
for _ in range(n - 2):
    points.append(list(map(float, sys.stdin.readline().split())))
points.append(end)

distance_matrix = [[0] * n for _ in range(n)]

for i in range(1, n):
    distance_matrix[0][i] = math.dist(start, points[i]) / 5
    distance_matrix[i][0] = distance_matrix[0][i]

for i in range(1, n):
    for j in range(i + 1, n):
        dist = math.dist(points[i], points[j])
        cannon_time = 2 + abs(dist - 50) / 5
        run_time = dist / 5
        time = min(run_time, cannon_time)
        distance_matrix[i][j] = time
        distance_matrix[j][i] = time

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

print(distance_matrix[0][-1])
