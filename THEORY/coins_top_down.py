import sys

infty = 1.0e8

# returns (min num coins, coins used)

#TODO COMPLETE THIS ALGO

def make_change(target, coins):
    if (cache[target][len(coins)] != )

    # base cases
    if target == 0:
        return (0, [])
    elif (len(coins) == 0):
        return (infty, [])
    
    use = (infty, [])
    if (target >= coins[0]):
        x = make_change(target - coins[0], coins) + 1
        use = (x[0] + 1, x[1] + [coins[0]])
    y = make_change(target, coins[1:])
    dont_use = y

    if (use[0] <= dont_use[0]):
        result = use
    else:
        result = dont_use
    
    cache[target][len(coins)] = result
    return result

