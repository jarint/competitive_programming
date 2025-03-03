import sys

# Read input
num_seats_left, num_weeks_left = map(int, sys.stdin.readline().strip().split())

# Store price and seat options per week
prices = [[] for _ in range(num_weeks_left + 1)]
seats = [[] for _ in range(num_weeks_left + 1)]

for i in range(num_weeks_left + 1):
    data = list(map(int, sys.stdin.readline().strip().split()))
    K = data[0]
    price_list = data[1:K+1]
    seat_list = data[K+1:2*K+1]
    prices[num_weeks_left - i] = price_list
    seats[num_weeks_left - i] = seat_list

# Memoization table initialized with -1
memo = [[-1] * (num_seats_left + 1) for _ in range(num_weeks_left + 1)]

def compute_max_revenue(weeks_left, seats_left):

    if weeks_left == -1:
        return 0  # No revenue can be made if no weeks are left
    if seats_left == 0:
        return 0  # No revenue can be made if no seats are left
    if memo[weeks_left][seats_left] != -1:
        return memo[weeks_left][seats_left]  # Return cached result

    max_revenue = 0
    for i in range(len(prices[weeks_left])):
        price = prices[weeks_left][i]
        num_tickets = seats[weeks_left][i]

        if seats_left >= num_tickets:
            revenue = price * num_tickets + compute_max_revenue(weeks_left - 1, seats_left - num_tickets)
        else:
            revenue = price * seats_left + compute_max_revenue(weeks_left - 1, 0)

        max_revenue = max(max_revenue, revenue)

    memo[weeks_left][seats_left] = max_revenue
    return max_revenue

# Compute the maximum possible revenue
max_revenue = compute_max_revenue(num_weeks_left, num_seats_left)

# Find the smallest price in the first week that achieves max revenue
optimal_price = 1001
for i in range(len(prices[num_weeks_left])):
    price = prices[num_weeks_left][i]
    num_tickets = seats[num_weeks_left][i]

    if num_seats_left >= num_tickets:
        revenue = price * num_tickets
        if num_weeks_left > 0:
            revenue += memo[num_weeks_left - 1][num_seats_left - num_tickets]
    else:
        revenue = price * num_seats_left
        if num_weeks_left > 0:
            revenue += memo[num_weeks_left - 1][0]

    if revenue == max_revenue:
        optimal_price = min(optimal_price, price)

print(max_revenue)
print(optimal_price)
