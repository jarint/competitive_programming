import sys


T = int(sys.stdin.readline().strip())

for i in range(T):
    sys.stdin.readline().strip()
    
    N = int(sys.stdin.readline().strip())
    num_candies = 0

    lines = N
    while lines > 0:
        c = sys.stdin.readline().strip()
        num_candies += int(c)
        lines -= 1
        
    if num_candies % N == 0:
        print("YES")
    else:
        print("NO")