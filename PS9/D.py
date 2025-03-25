import sys

vowels = 'AEIOU'
consonants = 'BCDFGHJKMNPQRSTVWXYZ'
combinations_map = {'V': 5, 'C': 20, 'L': 1}

word = list(sys.stdin.readline().strip())
masked_word = []
blank_positions = []

for i, letter in enumerate(word):
    if letter in vowels:
        masked_word.append('V')
    elif letter == 'L':
        masked_word.append('L')
    elif letter in consonants:
        masked_word.append('C')
    else:
        masked_word.append('_')
        blank_positions.append(i)

word_length = len(word)
answer = 0

def backtrack(current):
    global answer

    if len(current) == word_length:
        if 'L' in current:
            total_combinations = 1
            for pos in blank_positions:
                total_combinations *= combinations_map[current[pos]]
            answer += total_combinations
        return

    index = len(current)
    current_char = masked_word[index]
    C_L = ['C', 'L']

    if current_char != '_':
        if current_char in C_L and len(current) >= 2 and current[-1] in C_L and current[-2] in C_L:
            return
        if current_char == 'V' and len(current) >= 2 and current[-1] == 'V' and current[-2] == 'V':
            return
        backtrack(current + current_char)
    else:
        # consonant
        if not (len(current) >= 2 and current[-1] in C_L and current[-2] in C_L):
            backtrack(current + 'C')

        # L
        if not (len(current) >= 2 and current[-1] in C_L and current[-2] in C_L):
            backtrack(current + 'L')

        # vowel
        if not (len(current) >= 2 and current[-1] == 'V' and current[-2] == 'V'):
            backtrack(current + 'V')

backtrack('')
print(answer)
