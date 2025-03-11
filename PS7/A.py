import sys

num_straightaways, num_lanes = map(int, sys.stdin.readline().split())
lane_length, change_length = map(int, sys.stdin.readline().split())
sections = []

min_distance = [None] * (num_lanes + 1)
temp_distance = [None] * (num_lanes + 1)

first_lane_distance = int(sys.stdin.readline())
shift = 0
while first_lane_distance >= 0 and 1 + shift <= num_lanes:
    min_distance[1 + shift] = first_lane_distance + (change_length + lane_length) * shift
    shift += 1
    first_lane_distance -= lane_length

for _ in range(num_straightaways - 1):
    sections.append([int(sys.stdin.readline()), 0, 0])

for i in range(num_straightaways - 1):
    curve_data = sys.stdin.readline().split()
    sections[i][1] = int(curve_data[0])
    sections[i][2] = int(curve_data[1])

for section in sections:
    for i in range(1, len(min_distance)):
        if min_distance[i] is None:
            break
        min_distance[i] += section[1] + i * section[2] + section[0]
    
    temp_distance = min_distance.copy()
    for i in range(1, len(min_distance)):
        if min_distance[i] is None:
            break
        shift = 0
        remaining_length = section[0]
        
        while remaining_length >= 0 and i + shift <= num_lanes:
            possible_distance = (min_distance[i] - section[0]) + remaining_length + (change_length + lane_length) * shift
            temp_distance[i + shift] = possible_distance if temp_distance[i + shift] is None else min(temp_distance[i + shift], possible_distance)
            shift += 1
            remaining_length -= lane_length
        
        shift = 0
        remaining_length = section[0]
        while remaining_length >= 0 and i + shift > 0:
            possible_distance = (min_distance[i] - section[0]) + remaining_length + (change_length + lane_length) * abs(shift)
            temp_distance[i + shift] = possible_distance if temp_distance[i + shift] is None else min(temp_distance[i + shift], possible_distance)
            shift -= 1
            remaining_length -= lane_length
    
    min_distance = temp_distance.copy()

print(min_distance[1])
