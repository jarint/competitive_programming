import sys

def find_best_state(preferences, memo, priest_index, current_state):
    if priest_index == len(preferences):
        return current_state
    elif memo[priest_index][current_state] is not None:
        return memo[priest_index][current_state]

    best_state = None
    for flip in range(3):
        new_state = current_state ^ (1 << flip)
        result_state = find_best_state(preferences, memo, priest_index + 1, new_state)
        if best_state is None or preferences[priest_index][result_state] < preferences[priest_index][best_state]:
            best_state = result_state

    memo[priest_index][current_state] = best_state
    return best_state

input_data = sys.stdin.readlines()
num_rounds = int(input_data.pop(0))

for _ in range(num_rounds):
    num_priests = int(input_data.pop(0))
    priest_preferences = []
    for _ in range(num_priests):
        preferences = list(map(int, input_data.pop(0).split()))
        priest_preferences.append([p - 1 for p in preferences])
    
    memo = [[None] * 8 for _ in range(num_priests)]
    final_state = find_best_state(priest_preferences, memo, 0, 0)
    
    binary_state = f'{final_state:03b}'
    result = []
    for bit in binary_state:
        if bit == '1':
            result.append('Y')
        else:
            result.append('N')
    
    print("".join(result))
