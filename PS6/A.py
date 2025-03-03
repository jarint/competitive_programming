import sys

# load data
num_plates = int(sys.stdin.readline().strip())
plates = []

for i in range(num_plates):
    plates.append(int(sys.stdin.readline().strip()))


# memoization dictionary
memo = [{} for _ in range(num_plates)]

def closest_weight(index, current_sum):
    """
    For each plate in the plates array, there are two options:
    1. include that plate in the current_sum
    2. skip that plate and do not include it in the current_sum

    These are the two recursive calls on closest_weight()

    Base cases:
    1. if the index == num_plates:
            return the the current_sum - 1000 to show the difference
            from 1000.
    2. if current_sum >= 1000:
            return the current_sum - 1000 to show the difference from
            1000.
    
    To compute the answer: Choose the option with the minimal absolute
    difference from 1000. If the distance is the same, then pick the larger one

    store this answer in the memoization dictionary

    during each call of closest_weight, check the memoization array to see if
    that subproblem has already been computed
    """
    if index == num_plates:
        return current_sum - 1000
    
    if current_sum >= 1000:
        return current_sum - 1000
    
    # memoization array check
    if current_sum in memo[index]:
        return memo[index][current_sum]

    # option 1
    include = closest_weight(index + 1, current_sum + plates[index])

    # option 2
    skip = closest_weight(index + 1, current_sum)


    # choose the better option
    if abs(include) == abs(skip):
        result = max(include, skip)
    elif abs(include) > abs(skip):
        result = skip
    else:
        result = include
    
    #store it
    memo[index][current_sum] = result

    # return it
    return result



# return the difference of the optimal solution from 1000 and add
# 1000 to it to return the closest weight.
print(closest_weight(0, 0) + 1000)
