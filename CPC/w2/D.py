import sys

num_teams = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))

temp = []
for index, value in enumerate(times):
    temp.append((value, index))

ante_order = sorted(temp)
goran_order = ante_order[::-1]

ttime_ante = 0
ttime_goran = 0

# greedy heuristic: ante goes least time to most, goran does exact reverse
for i in range(num_teams):
    if ante_order[i][1] != goran_order[i][1]:
        ttime_ante += ante_order[i][0]
        ttime_goran += goran_order[i][0]
    else:
        # hit same index
        ttime_goran += goran_order[i][0]
        ttime_ante += (ante_order[i][0] - ante_order[i-1][0]) + ante_order[i][0]

out = max(ttime_ante, ttime_goran)
print(out)

