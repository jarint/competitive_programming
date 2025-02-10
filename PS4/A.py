import sys

N, Q = map(int, sys.stdin.readline().strip().split())
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
current = 2

while current * current <= N:
    if is_prime[current]:
        for idx in range(current * current, N + 1, current):
            is_prime[idx] = False
    current += 1

print(sum(is_prime))

for line in sys.stdin:
    query_num = int(line)
    if is_prime[query_num]:
        print(1)
    else:
        print(0)