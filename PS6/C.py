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

memo = [[-1] * (num_seats_left + 1) for _ in range(num_weeks_left + 1)]

# DP Function
def find_max_revenue(weeks_left, seats_left):
    if weeks_left == -1:
        return 0
    if seats_left == 0:
        memo[weeks_left][seats_left] = 0
        return 0
    if memo[weeks_left][seats_left] != -1:
        return memo[weeks_left][seats_left]

    max_revenue = 0
    for i in range(len(prices[weeks_left])):
        price = prices[weeks_left][i]
        num_tickets = seats[weeks_left][i]

        if seats_left >= num_tickets:
            revenue = price * num_tickets
            if weeks_left > 0 and (seats_left - num_tickets) >= 0:
                revenue += find_max_revenue(weeks_left - 1, seats_left - num_tickets)
        else:
            revenue = price * seats_left
            if weeks_left > 0:
                revenue += find_max_revenue(weeks_left - 1, 0)

        max_revenue = max(max_revenue, revenue)

    memo[weeks_left][seats_left] = max_revenue
    return max_revenue

max_revenue = find_max_revenue(num_weeks_left, num_seats_left)

best_price = 1001  
for i in range(len(prices[num_weeks_left])):
    price = prices[num_weeks_left][i]
    num_tickets = seats[num_weeks_left][i]

    if num_seats_left >= num_tickets:
        revenue = price * num_tickets
        if num_weeks_left > 0 and (num_seats_left - num_tickets) >= 0:
            revenue += memo[num_weeks_left - 1][num_seats_left - num_tickets]
    else:
        revenue = price * num_seats_left
        if num_weeks_left > 0:
            revenue += memo[num_weeks_left - 1][0]

    if revenue == max_revenue:
        best_price = min(best_price, price)

print(max_revenue)
print(best_price)
