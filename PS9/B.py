import sys

# try to precompute where each number can go to instead
legal_moves = [
    [0],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [2, 3, 5, 6, 8, 9, 0],
    [3, 6, 9],
    [4, 5, 6, 7, 8, 9, 0],
    [5, 6, 8, 9, 0],
    [6, 9],
    [7, 8, 9, 0],
    [8, 9, 0],
    [9]
]

def is_legal(number):
    digits = [int(d) for d in str(number)]
    for i in range(len(digits) - 1):
        if digits[i + 1] not in legal_moves[digits[i]]:
            return False
    return True

input_lines = sys.stdin.read().strip().split('\n')
test_case_count = int(input_lines[0])
line_index = 1

for _ in range(test_case_count):
    target = int(input_lines[line_index])
    line_index += 1

    for offset in range(target + 1):
        if is_legal(target + offset):
            print(target + offset)
            break
        if target - offset >= 0 and is_legal(target - offset):
            print(target - offset)
            break
