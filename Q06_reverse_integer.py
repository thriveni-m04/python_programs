# Question 6: Reverse Integer
# Given a signed 32-bit integer x, reverse its digits.
# If the reversed integer is outside the range
# [-2^31, 2^31 - 1], return 0.

x = -123

# Store the sign of the number
if x < 0:
    sign = -1
else:
    sign = 1

# Reverse the absolute value
reversed_num = int(str(abs(x))[::-1])

# Restore the original sign
result = sign * reversed_num

# Define the signed 32-bit integer limits
minimum = -(2 ** 31)
maximum = (2 ** 31) - 1

# Check whether the result is within the valid range
if minimum <= result <= maximum:
    print("Reversed Integer:", result)
else:
    print("Reversed Integer: 0")
