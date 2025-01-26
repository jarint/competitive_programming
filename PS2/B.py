import sys

LIMIT = 300

num_probs = 0
first_solve = None
time_estimates = []

def read_input():
    global num_probs, first_solve
    line1 = sys.stdin.readline().strip()
    num_probs, first_solve = map(int, line1.split())
    
    line2 = sys.stdin.readline().strip()
    for est in line2.split():
        time_estimates.append(int(est))


def score_check(num_probs, first_solve, time_estimates):
    Num_AC = 0
    Penalty_Time = 0
    
    time_remain = 300
    
    if (time_estimates[first_solve] > LIMIT):
        return Num_AC, Penalty_Time
    else:
        Num_AC += 1
        Penalty_Time += time_estimates[first_solve]
        time_remain = time_remain - time_estimates[first_solve]
        time_estimates.pop(first_solve)
    
    # sort the time_estimates list
    time_estimates.sort()
    
    # now iterate and check how many you can solve
    current_time = Penalty_Time
    for i in range(len(time_estimates)):
        if (time_estimates[i] <= time_remain):
            Num_AC += 1
            Penalty_Time += current_time + time_estimates[i]
            time_remain = time_remain - time_estimates[i]
            current_time = current_time + time_estimates[i]
    
    return Num_AC, Penalty_Time

read_input()
Num_AC, Penalty_Time = score_check(num_probs, first_solve, time_estimates)
print(f"{Num_AC} {Penalty_Time}")