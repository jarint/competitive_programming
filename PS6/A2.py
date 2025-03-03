import sys

num_plates = int(sys.stdin.readline().strip())
plates = [int(sys.stdin.readline().strip()) for _ in range(num_plates)]

possible_sums = {0} # use a set?

for weight in plates:
    new_sums = set()
    for current_sum in possible_sums:
        new_sums.add(current_sum + weight)
    possible_sums.update(new_sums)


best_weight = min(possible_sums, key=lambda x: (abs(x - 1000), -x))

print(best_weight)
