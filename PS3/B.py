import sys
from decimal import Decimal

MAX_PAYMENTS = 1200

n = int(sys.stdin.readline().strip())


def APR(R, B, M):
    num_payments = 0
    
    while B > 0:
        original = B
        new_interest = round(B * (R / 100), 2)
        B += new_interest
        B -= M
        num_payments += 1

        if B >= original:
            return -1
        
        if num_payments > MAX_PAYMENTS:
            return -1
    
    return num_payments
    

for i in range(n):
    R, B, M = map(Decimal, sys.stdin.readline().strip().split())
    
    apr = APR(R, B, M)

    if apr == -1:
        print("impossible")
    else:
        print(str(apr))