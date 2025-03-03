import sys

# Read input
num_plates = int(sys.stdin.readline().strip())
plates = [int(sys.stdin.readline().strip()) for _ in range(num_plates)]

# Use a set to track reachable sums
possible_sums = {0}

for weight in plates:
    new_sums = set()
    for current_sum in possible_sums:
        new_sums.add(current_sum + weight)
    possible_sums.update(new_sums)

# Find the best weight closest to 1000
best_weight = min(possible_sums, key=lambda x: (abs(x - 1000), -x))

print(best_weight)
