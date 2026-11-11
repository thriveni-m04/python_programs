
# Q42. House Robber

def rob_houses(nums):
    previous = 0
    current = 0

    for money in nums:
        # Choose between robbing this house or skipping it
        new_current = max(current, previous + money)

        previous = current
        current = new_current

    return current


# Sample input
nums = [1, 2, 3, 1]

print("Maximum Money:", rob_houses(nums))
