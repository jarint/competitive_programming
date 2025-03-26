import sys

num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
  n, m = map(int, sys.stdin.readline().strip().split())
  for i in range(m):
    l = list(map(int, sys.stdin.readline().strip().split()))
  print(n - 1)
