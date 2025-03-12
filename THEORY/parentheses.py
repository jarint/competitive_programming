import sys

found = set()
OFFSET = 3000

def count(index, par, val):
    if
    
    
    if index == n:
        found.add(val)
        return

    if (par % 2 == 0): # even parentheses level
        new_val = val + nums[index]
    
    else:
        new_val = val - nums[index]
    
    if (nums[index] < 0):
        count(index + 1, par + 1, val = new_val)

    if (par > 0):
        count(index + 1, par - 1, new_val) # option to close the parenthesis
    
    count(index + 1, par, new_val)
    cache[index][par][val + OFFSET] = 1

symbols = sys.stdin.readline().split()
nums = []

sign = 1 

for s in symbols:

    if (s == '+'):
        sign = 1
    elif (s == '-'):
        sign = -1
    else:
        nums.append(sign * int(s))

print(nums)



n = len(nums)


cache = [{[-1 for i in range(6001)] for j in range(n+1))] # some kind of issue with this
count(0,0,0)
