import sys
import math


# this wont work, use cpp instead
def isPrime(n):
    d = 2
    while d*d <= n:
        while (n % d) == 0:            
            n //= d
        d += 1
    if n > 1:       
        return True
    else:
        return False

def factor(n):
    pass

for line in sys.stdin:
    num = int(line)
    if num == 4:
        sys.exit()
    elif isPrime(num):
        print(num)
        continue
    else:
        factor(num)