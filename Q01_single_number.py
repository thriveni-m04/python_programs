# Question 1: Single Number
# Given a non-empty array of integers, every element appears twice
# except one element. Find the element that appears only once.
# Use linear time complexity and constant extra space.

nums = [4, 1, 2, 1, 2]

# Initialize result with 0
result = 0

# XOR every element in the array
for num in nums:
    result = result ^ num

# The remaining number is the single number
print("Single Number:", result)

