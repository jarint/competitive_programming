import sys

n, d = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
new_nums = [num // d for num in nums]


array = nums[1].split()
for i in range(n):
    array[i] = int(array[1]) // d

total = 0

# can't use double for loop, too slow
counts = []
for i in range(n):
    if array[i] in counts:
        counts[array[i]] += 1
    else:
        counts[array[i]] = 1

for val in counts:
    pass

