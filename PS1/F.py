import sys
import math


high = 1000
low = 1

def guess (lowguess, highguess):
    mid = (highguess+lowguess) // 2
    return mid

def responseCheck(response, current_guess):
    global high, low
    if response == "lower":
        high = current_guess - 1
    elif response == "higher":
        low = current_guess + 1
    elif response == "correct":
        sys.exit()

while True:
    current_guess = guess(low,high)
    sys.stdout.write(str(current_guess) + "\n")
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    responseCheck(response, current_guess)