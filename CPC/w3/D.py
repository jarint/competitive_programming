#import sys
#
#Q, M, S, L = map(int, sys.stdin.readline().strip().split())
#
#to_schedule = [Q] * L + [1] * S
#
#slots = [0] * M
#active = 0
#tick = 0
#while active > 0 or to_schedule:
#    for i in range(M):
#        if (slots[i] == 0) and to_schedule:
#            slots[i] = to_schedule.pop(0)
#            active += 1
#
#    next = min([t for t in slots if t > 0], default = 1)
#    tick += next
#
#    for i in range(M):
#        if slots[i] > 0:
#            slots[i] -= next
#        if slots[i] == 0:
#            active -= 1
#
#print(tick)

import sys

def solve(q, m, s, l):
    """
    Computes the minimum time required to complete all tasks
    given:
    - q: Time required to complete one long task
    - m: Number of available machines
    - s: Number of short (1-second) tasks
    - l: Number of long (q-second) tasks
    """

    total_time = 0  # Tracks the total time taken

    # **Step 1: Distribute as many long tasks (L) as possible across all M machines**
    if l >= m:
        # Each full batch of `m` machines takes `q` seconds
        total_time += (l // m) * q  
        # Reduce L to the remaining unassigned long tasks
        l %= m  

    # **Step 2: If no long tasks remain, process short tasks (S) directly**
    if l == 0:
        # Short tasks are distributed across all machines
        total_time += (s // m)  # Full batches take exactly 1 second each
        # If there are leftover short tasks, add 1 extra second
        return total_time + (1 if s % m != 0 else 0)

    # **Step 3: Allocate the remaining long tasks**
    # Since `l < m`, we need one more `q`-second batch to process them
    total_time += q  

    # **Step 4: Use the remaining machines (`m - l`) to process short tasks**
    # These extra machines can complete `short_tasks = (m - l) * q` in the same cycle
    s -= (m - l) * q  # Reduce `s` accordingly

    # **Step 5: If all short tasks are done, return the total time**
    if s <= 0:
        return total_time

    # **Step 6: Spread the remaining short tasks across machines**
    total_time += (s // m)  # Full machine cycles
    # If there are leftover short tasks, add 1 extra second
    return total_time + (1 if s % m != 0 else 0)


# Read input values
q, m, s, l = map(int, sys.stdin.readlines().strip().split())

# Compute and print the total completion time
print(solve(q, m, s, l))