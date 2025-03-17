import sys
from datetime import datetime
from itertools import permutations


num_test_cases = int(sys.stdin.readline().strip())
born_date = datetime(2000, 1, 1)

for _ in range(num_test_cases):
    digit_string = sys.stdin.readline().strip().replace(" ", "")
    valid_dates = set()
    
    for perm in set(permutations(digit_string)):
        if len(perm) != 8:
            continue

        day = int(perm[0] + perm[1])
        month = int(perm[2] + perm[3])
        year = int("".join(perm[4:]))

        if year < 2000 or not (1 <= month <= 12) or not (1 <= day <= 31):
            continue

        try:
            date_object = datetime(year, month, day)
            valid_dates.add(date_object)
        except:
            pass

    if valid_dates:
        earliest_date = min(valid_dates)
        print(len(valid_dates), earliest_date.strftime("%d %m %Y"))
    else:
        print(0)
