import sys
from fractions import Fraction

n = sys.stdin.readline().strip()

coefficients = list(map(int, sys.stdin.readline().strip().split()))

def calc(coefficients):
    if len(coefficients) == 1:
        return coefficients[0], 1
    x0 = coefficients[0]
    coefficients.pop(0)

    n, d = calc(coefficients)

    numerator = x0 * n + d
    denominator = n

    return numerator, denominator

numerator, denominator = calc(coefficients)
answer = Fraction(numerator, denominator)
print(answer)
