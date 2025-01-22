import sys

for line in sys.stdin:
    line = line.strip()

    a, b = map(int, line.split())
    print(abs(a - b))
