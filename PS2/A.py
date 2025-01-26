import sys

PENALTY = 20

right_counter = 0
time = 0

results = []
right = []
wrong = []

for line in sys.stdin:
    line = line.strip()
    if line == "-1":
        break
    a, b, c = line.split()
    results.append((a, b, c))

def count_right_and_wrong():
    global right_counter, time
    for result in results:
        if result[2] == "right":
            right_counter += 1
            time += int(result[0])
            right.append(result)
        else:
            wrong.append(result)
    
def calculate_penalties():
    global time
    for r in right:
        for w in wrong:
            if r[1] == w[1]:
                time += PENALTY

count_right_and_wrong()
calculate_penalties()
print(f"{right_counter} {time}")