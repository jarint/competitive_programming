import sys
import math

N = int(sys.stdin.readline().strip())
coords = []

for _ in range(N):
    xi, yi = map(int, sys.stdin.readline().strip().split())
    coords.append((xi, yi))

mean_x = sum(x for x, y in coords) / N
mean_y = sum(y for x, y in coords) / N

#print(mean_x, mean_y)

#SS_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in coords)
#SS_xx = sum((xi - mean_x) * (xi - mean_x) for xi, yi in coords)

#print(SS_xy, SS_xx)

b_1 = 1
b_0 = mean_y - (b_1 * mean_x)

print(b_0)