import sys

def extended_gcd(a, b):
    coeff_x, coeff_y = 0, 1
    prev_x, prev_y = 1, 0
    
    while a != 0:
        quotient = b // a
        remainder = b % a
        temp_x = coeff_x - prev_x * quotient
        temp_y = coeff_y - prev_y * quotient
        b, a = a, remainder
        coeff_x, coeff_y = prev_x, prev_y
        prev_x, prev_y = temp_x, temp_y
    
    return b, coeff_x, coeff_y


test_cases = int(sys.stdin.readline().strip())
for _ in range(test_cases):
    
    K, C = map(int, sys.stdin.readline().strip().split())
    gcd_val, factor, x_val = extended_gcd(C, K)
    
    if gcd_val != 1:
        print("IMPOSSIBLE")
        continue
    
    if x_val == 0:
        factor += K // gcd_val
    
    if factor > 0:
        print(factor)
        continue
    
    adjustment = (-factor * gcd_val // K) + 1
    print(factor + (adjustment * (K // gcd_val)))
