import sys


C, n = map(int, sys.stdin.readline().strip().split())
tups = []

for i in range(n):
    num_left, num_entered, num_wait = map(int, sys.stdin.readline().strip().split())
    tups.append((num_left, num_entered, num_wait))

def check(C, tups):
    # check last station waiting. If > 0, return False
    if tups[-1][2] > 0:
        return False
    
    # check that train is empty at first stations --
    # the number that left is 0 at first station
    if tups[0][0] != 0:
        return False
    
    curr_on_board = 0
    for train in tups:
        left = train[0]
        entered = train[1]
        wait = train[2]
        curr_on_board -= left
        if curr_on_board < 0:
            return False
        curr_on_board += entered
        if curr_on_board > C:
            return False
        # no passenger waits in vain
        if (curr_on_board < C) and (wait > 0):
            return False
    # train needs to empty at the end
    if curr_on_board > 0:
        return False
    
    return True

if check(C, tups):
    print("possible")
else:
    print("impossible")