import sys

line = sys.stdin.readline().strip().split("-")
Ans = ""

for i in range(len(line)):
    Ans += line[i][0]

print(Ans)