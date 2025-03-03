import sys

# Read input
num_plates = int(sys.stdin.readline().strip())
plates = [int(sys.stdin.readline().strip()) for _ in range(num_plates)]

# Use a set for memoization
visited_weights = set()

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
    
    # Check if this state has already been visited
    if (index, current_sum) in visited_weights:
        return float('inf')  # Return a large value to avoid recomputation

    # Mark this state as visited
    visited_weights.add((index, current_sum))

    # Option 1: Include the current plate
    include = closest_weight(index + 1, current_sum + plates[index])

    # Option 2: Skip the current plate
    skip = closest_weight(index + 1, current_sum)

    # Choose the better option
    if abs(include) == abs(skip):
        result = max(include, skip)
    elif abs(include) > abs(skip):
        result = skip
    else:
        result = include

    return result

print(closest_weight(0, 0) + 1000)
