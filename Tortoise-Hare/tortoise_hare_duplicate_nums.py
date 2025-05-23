# https://leetcode.com/problems/find-the-duplicate-number/description/

nums = [4, 3, 7, 8, 6, 9, 2, 1, 5, 2]

def tortoiseHare(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = hare 

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1 

# Array can be accepted if two conditions are met:
# 1) values in the array need to be 1 .. n
# 2) array size needs to be n + 1
# Satisfying these conditions ensure that at least one duplicate value
# exists in the array via the pigeonhole principle.
nums = [4, 3, 7, 8, 6, 9, 2, 1, 5, 2]
print(f"Tortoise and Hare: {tortoiseHare(nums)}")

# bottomless pit
def fourlewp(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                if nums[i] == nums[j]:
                    return nums[j]
print(f"double for loop: {fourlewp(nums)}")

# seen array
def seenarray(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True
print(f"seen array: {seenarray(nums)}")
