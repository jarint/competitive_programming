# iterative fib

import sys

n = int(sys.stdin.readline())

fib = [1,1]
# want fib[i] is ith fibonacci number

for i in range(2, n):
    fib[i] = fib[i-1] + fib[i-2]

