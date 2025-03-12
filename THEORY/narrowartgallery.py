import sys

infty = 10e8

def block(row, prev, k):
    # check cache first
    if cache[row][prev][k] != -1:
        return cache[row][prev][k]
    
    if k == 0:
        return 0 # no rooms left to block
    
    elif (row >= n):
        return infty
    
    donothing = block(row+1, 0, k)

    if (prev == 1):
        right = block(row + 1, 1, k-1) + rooms[row][1]
    if (prev == 2):
        left = block(row + 1, 2, k-1) + rooms[row][0]
    if (prev == 0):
        right = block(row + 1, 1, k-1) + rooms[row][1]
        left = block(row + 1, 2, k-1) + rooms[row][0]
    
    result = min(donothing, left, right)
    cache[row][prev][k] = result
    return result

data = sys.stdin.read().split()

n = int(data[0])
k = int(data[1])

rooms = []
total_val = 0

for i in range(2, 2*n, 2, 2):
    total_val += int(data[i]) + int(data[i+1])
    rooms.append((int(data[i]), int(data[i+1])))

print(rooms)

cache = [[-1 for i in range(k+1)] for j in range(4) for _ in range(n+1)]
print(total_val - block(0,0,k))
