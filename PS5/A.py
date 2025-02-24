import fileinput
import math

# memoization approach
limit = int(1e6 + 1)
cap = int (1e5)
precomp = [0]*limit
precomp[0] = 1
precomp[1] = 1

def shorten(n):
    while n % 10 == 0:
        n //= 10
    return n % cap

def get_right_non_zero(n):
    while n % 10 == 0:
        n //= 10
    return n % 10

## precomputation
current = 1
for i in range( 2, limit):
    current *= i
    current = shorten(current)
    precomp[i] = get_right_non_zero(current)

to_zero = []
for line in fileinput.input():
    line = int(line.strip())
    to_zero.append(line)

for n in to_zero:
    if n == 0:
        continue
    else:
        print(precomp[n])
