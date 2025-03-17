import sys

num_cases = int(sys.stdin.readline().strip())
input_data = sys.stdin.read().splitlines()

for case_index in range(num_cases):
    island_count = 0
    sequence = list(map(int, input_data[case_index].split()))[1:]

    for start in range(1, 11):
        for end in range(start, 11):  
            is_island = True
            for index in range(start, end + 1):
                # If any element in the subsequence is <= to neighboring elements (not a local peak),
                # then not an island
                if sequence[index] <= sequence[start - 1] or sequence[index] <= sequence[end + 1]:
                    is_island = False
                    break
            if is_island:
                island_count += 1  

    print(case_index + 1, island_count)
