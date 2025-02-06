import sys
import math

a,b = sys.stdin.readline().strip().split("/")
a = int(a)
b = int(b)

gcd = math.gcd(a,b)

new_numerator = a // gcd
new_denom = b // gcd

subtract = 32*new_denom

mid_numerator = new_numerator - subtract
n = mid_numerator * 5
d = new_denom * 9

new_gcd = math.gcd(n,d)

n = n // new_gcd
d = d // new_gcd

print(f"{n}/{d}")
