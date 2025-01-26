import sys
from collections import defaultdict

card_locations = {}
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

for i in range(K):
    C1, C2, P1, P2 = sys.stdin.readline().strip().split()
    card_locations[C1] = P1
    card_locations[C2] = P2
    if P1 == P2:
        card_locations.pop(C1)
        card_locations.pop(C2)
        N -= 2

count_dict = defaultdict(int)
for k, v in card_locations.items():
    count_dict[v] += 1

paired = 0
unpaired = 0

for k, v in count_dict.items():
    if v == 2:
        paired += 1
    elif v==1:
        unpaired += 1

seen = paired + unpaired

if N == 2*seen:
    paired += unpaired
elif N == 2*paired + 2:
    paired += 1

print(paired)