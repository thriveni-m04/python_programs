# Q11. Missing Number
# Find the missing number from an array containing numbers from 0 to n.

nums = [3, 0, 1]

# Find the expected sum of numbers from 0 to n.
n = len(nums)
expected_sum = n * (n + 1) // 2

# Find the actual sum of the given array.
actual_sum = sum(nums)

# The difference gives the missing number.
missing = expected_sum - actual_sum

print("Missing Number:", missing)