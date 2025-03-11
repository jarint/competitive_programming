import sys
from math import inf

num_instruments, num_notes = map(int, sys.stdin.readline().split())
instrument_sets = [set(map(int, sys.stdin.readline().split()[1:])) for _ in range(num_instruments)]
note_sequence = list(map(int, sys.stdin.readline().split()))

memo = [[inf] * num_instruments for _ in range(num_notes)]
min_switches = [1]

for i in range(num_instruments):
    if note_sequence[0] in instrument_sets[i]:
        memo[0][i] = 0

for i in range(1, num_notes):
    for j in range(num_instruments):
        if note_sequence[i] in instrument_sets[j] and note_sequence[i - 1] in instrument_sets[j]:
            memo[i][j] = memo[i - 1][j]
        memo[i][j] = min(memo[i][j], min_switches[-1] + 1)
    min_switches.append(min(memo[i]))

print(min(memo[-1]))
