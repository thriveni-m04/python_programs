# Q18. Maximum Product Subarray
# Find the maximum product of a contiguous subarray.

nums = [2, 3, -2, 4]

# Initially, both maximum and minimum products are the first element.
max_product = nums[0]
min_product = nums[0]

# Store the final maximum product.
result = nums[0]

for i in range(1, len(nums)):

    # A negative number can change the maximum into minimum and vice versa.
    if nums[i] < 0:
        max_product, min_product = min_product, max_product

    # Calculate the new maximum product.
    max_product = max(nums[i], max_product * nums[i])

    # Calculate the new minimum product.
    min_product = min(nums[i], min_product * nums[i])

    # Update the final answer.
    result = max(result, max_product)

print("Maximum Product:", result)