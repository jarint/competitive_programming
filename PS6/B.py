import sys

# input handling
n = int(sys.stdin.readline().strip())
weights = []
for i in range(n):
    weights.append(int(sys.stdin.readline().strip()))

if n == 0:
    print(0)
    sys.exit()

longest_increasing_sequence = [1] * n
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if weights[j] > weights[i]:
            longest_increasing_sequence[i] = max(longest_increasing_sequence[i], 1 + longest_increasing_sequence[j])

longest_decreasing_sequence = [1] * n
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if weights[j] < weights[i]:
            longest_decreasing_sequence[i] = max(longest_decreasing_sequence[i], 1 + longest_decreasing_sequence[j])

result = 0
for i in range(n):
    result = max(result, longest_increasing_sequence[i] + longest_decreasing_sequence[i] - 1)

print(result)
