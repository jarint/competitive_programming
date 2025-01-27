import sys

Birthdays = []
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def insert_birthday(date):
    global Birthdays
    month, day = map(int, date.split("-"))
    Birthdays.append([month, day])

def find_longest_gap():
    global Birthdays
    current_month, current_day = min(Birthdays)
    current_month -= 1

    longest_gap = 0
    max_gap_length = 0
    gaps = []
    total_days = sum(days_in_month)

    for _ in range(total_days):
        longest_gap += 1
        prev_month, prev_day = current_month, current_day
        if current_day + 1 > days_in_month[current_month]:
            current_day = 1
            current_month += 1
            if current_month == 12:
                current_month = 0
        else:
            current_day += 1

        if [current_month + 1, current_day] in Birthdays:
            if longest_gap > max_gap_length:
                max_gap_length = longest_gap
                gaps = [[prev_month + 1, prev_day]]
            elif longest_gap == max_gap_length:
                gaps.append([prev_month + 1, prev_day])
            longest_gap = 0

    if len(gaps) == 1:
        return gaps[0]

    min_distance = total_days
    reference_month, reference_day = 9, 27
    closest_gap = []

    for month, day in gaps:
        month -= 1
        distance = None
        if month < reference_month:
            distance = 5 + sum(days_in_month[10:]) + sum(days_in_month[:month]) + day
        elif month > reference_month:
            distance = 27 + sum(days_in_month[10:month]) + day
        else:
            if day <= reference_day:
                distance = total_days - (reference_day - day)
            else:
                distance = day - reference_day
        if distance < min_distance:
            min_distance = distance
            closest_gap = [month + 1, day]

    return closest_gap

def format_output(gap):
    month, day = gap
    month, day = map(str, [month, day])
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    print(month + '-' + day)


N = int(sys.stdin.readline().strip())
for _ in range(N):
    _, date = sys.stdin.readline().strip().split()
    insert_birthday(date)

gap = find_longest_gap()
format_output(gap)