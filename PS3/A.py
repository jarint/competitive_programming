import sys
import math


m, n, t = sys.stdin.readline().strip().split()
m, n = int(m), int(n)

def complexity(t, n, m):
    match t:
        case "1":
            if n >= 13:
                return m + 1
            else:
                return math.factorial(n)
        case "2":
            if n >= 30:
                return m + 1
            else:
                return pow(2, n)
        case "3":
            return pow(n, 4)
        case "4":
            return pow(n, 3)
        case "5":
            return pow(n, 2)
        case "6":
            return n*math.log(n, 2)
        case "7":
            return n


ops = complexity(t, n, m)
if ops <= m:
    print("AC")
else:
    print("TLE")
