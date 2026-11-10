# Q33. Plus One
# Add 1 to a number represented as a list of digits.

digits = [1, 2, 3]

# Start from the last digit
for i in range(len(digits) - 1, -1, -1):

    if digits[i] < 9:
        digits[i] += 1
        break

    else:
        # If digit is 9, make it 0 and carry 1
        digits[i] = 0

else:
    # If all digits were 9, add 1 at the beginning
    digits.insert(0, 1)

print("Updated Digits:", digits)

# Sample Input:
# [1, 2, 3]
#
# Expected Output:
# Updated Digits: [1, 2, 4]