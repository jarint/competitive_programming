import sys
from collections import defaultdict

prev_animal = sys.stdin.readline().strip()[-1]
num_names = int(sys.stdin.readline())
name_list = []
by_start = defaultdict(list)

for i in range(num_names):
    name = sys.stdin.readline().strip()
    name_list.append(name)
    by_start[name[0]].append(i)

if prev_animal not in by_start:
    print("?")
    sys.exit()

for idx in by_start[prev_animal]:
    name = name_list[idx]
    end_char = name[-1]
    if end_char not in by_start or (end_char == name[0] and len(by_start[end_char]) == 1):
        print(name + "!")
        sys.exit()

print(name_list[by_start[prev_animal][0]])
