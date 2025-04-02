import sys

ds, ys = map(int, sys.stdin.readline().strip().split())
dm, ym = map(int, sys.stdin.readline().strip().split())

num_years = 0
while ds != 0 or dm != 0:
    num_years += 1
    ds = (ds+1) % ys
    dm = (dm+1) % ym
print(num_years)
