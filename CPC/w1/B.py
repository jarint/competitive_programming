import sys
import math

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

N = int(sys.stdin.readline().strip())

if N == 1:
    print("Either")
elif N == 2:
    print("Odd")
elif (N % 2 == 0):
    if is_power_of_two(N):
        print ("Even")
    else:
        print ("Odd")
else:
    print("Either")