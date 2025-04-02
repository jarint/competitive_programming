import sys 

num_teams, num_teams_damaged, num_teams_reserve = map(int, sys.stdin.readline().strip().split()) #not used
damaged_kayaks = list(map(int, sys.stdin.readline().strip().split()))
reserve_kayaks = list(map(int, sys.stdin.readline().strip().split()))


# check if team with damaged kayaks
# can borrow one from their neighbours
can_borrow = 0
for current in damaged_kayaks:
    right = current + 1
    left = current - 1
    if left in reserve_kayaks:
        reserve_kayaks.remove(left)
        can_borrow += 1
    elif right in reserve_kayaks:
        reserve_kayaks.remove(right)
        can_borrow += 1
print(len(damaged_kayaks) - can_borrow)
