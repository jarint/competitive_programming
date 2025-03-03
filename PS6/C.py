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

# memoization - memo[w][s] stores the maximum revenue possible for
# w weeks and s available seats left
memo = [[-1] * (num_seats_left + 1) for _ in range(num_weeks_left + 1)]

# DP
def find_max_revenue(weeks_left, seats_left):
    
    # Base cases:
    # 1. if weeks left is -1, we've processed all weeks, return 0
    if weeks_left == -1:
        return 0
    # if seats left is 0, all tickets are sold, return 0.
    if seats_left == 0:
        return 0
    # if the result is already computed then just return it
    if memo[weeks_left][seats_left] != -1:
        return memo[weeks_left][seats_left]

    max_revenue = 0
    for i in range(len(prices[weeks_left])):
        price = prices[weeks_left][i]
        num_tickets = seats[weeks_left][i]

        # there are more seats than tickets
        if seats_left >= num_tickets:
            revenue = price * num_tickets + find_max_revenue(weeks_left - 1, seats_left - num_tickets)
        # there are fewer seats than tickets
        else:
            revenue = price * seats_left + find_max_revenue(weeks_left - 1, 0)
        
        max_revenue = max(max_revenue, revenue)
    
    #store in memo array
    memo[seats_left][weeks_left] = max_revenue

max_revenue = find_max_revenue(num_weeks_left, num_seats_left)

best_price = 1001 # initialize at 1 more than max price allowed, arbitrary
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
        optimal_price = min(best_price, price)
