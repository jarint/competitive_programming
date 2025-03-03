import sys

# Input handling
N = int(sys.stdin.readline().strip())
test_cases = []

for i in range(N):
    num_distances = int(sys.stdin.readline().strip())
    distances = list(map(int, sys.stdin.readline().strip().split()))
    test_cases.append((num_distances, distances))

# Solution using DP
for num_distances, distances in test_cases:
    total_distance = sum(distances)

    # DP table: (direction, max height reached)
    dp = [[("-", 0)] * (total_distance + 1) for _ in range(num_distances)]
    dp[0][distances[0]] = ("U", distances[0])

    # DP
    for i in range(1, num_distances):
        d = distances[i]
        for h in range(total_distance + 1):
            
            # climbing down
            if h + d <= total_distance:
                direction, max_height = dp[i - 1][h + d]
                if direction != "-":
                    dp[i][h] = ("D", max_height)

            # climbing up
            if h >= d:
                direction, max_height = dp[i - 1][h - d]
                max_height = max(max_height, h)
                if direction != "-":
                    curr_direction, curr_max_height = dp[i][h]
                    if curr_direction == "-" or curr_max_height > max_height:
                        dp[i][h] = ("U", max_height)

    # Check if end at height 0 is possible
    if dp[num_distances - 1][0][0] == "-":
        print("IMPOSSIBLE")
        continue

    # Backtrack to find path
    height = 0
    solution = []

    for i in range(num_distances - 1, -1, -1):
        move, _ = dp[i][height]
        solution.append(move)
        if move == 'U':
            height -= distances[i]
        else:
            height += distances[i]

    # Reverse the solution for correct order
    print("".join(solution[::-1]))
