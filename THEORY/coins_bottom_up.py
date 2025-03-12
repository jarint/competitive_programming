import sys

infty = 1.0e8

buff = sys.stdin.read().split()
target = int(buff[0])
ncoins = int(buff[1])

index = 2
coins = []

for i in range(ncoins):
    coins.append(int(buff[index]))
    index += 1

print()

#cache

cache = [[-1 for i in range (ncoins+1)] for j in range(target + 1)]

#base cases

#1
for i in range(ncoins + 1):
    cache[0][i] = 0


#2
for i in range(target + 1):
    cache[i][0] = infty


cache[0][0] = 0


for i in range(1, target + 1):
    for j in range(1, ncoins+1):

        use = infty
        if (coins[j] <= i):
            use = cache[i - coins[j-1]][j] + 1
        dont_use = cache[i][j-1]

        cache[i][j] = min(use, dont_use)

print(cache[target][ncoins])
