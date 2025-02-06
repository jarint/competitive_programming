import sys


## TO SLOW !!!!!!!!!


n, d = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

pairs = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        ai = nums[i]
        aj = nums[j]
        if (ai // d) == (aj // d):
            pairs.append((ai, aj))

print(len(pairs))
