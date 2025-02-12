import sys

n = int(sys.stdin.readline().strip())
citations = []

for i in range(n):
    c = int(sys.stdin.readline().strip())
    citations.append(c)
    
sort_cits = sorted(citations, reverse=True)

h = 0
for i in range(n):
    if sort_cits[i] >= (i + 1):
        h = i+1

print(h)