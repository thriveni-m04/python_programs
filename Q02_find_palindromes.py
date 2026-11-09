# Question 2: Find Palindromes in a Given Range
# Given two integers m and n, find all palindrome numbers
# within the range [m, n], including both endpoints.

m = 10
n = 50

palindromes = []

# Check every number in the given range
for num in range(m, n + 1):

    # Convert the number into a string
    value = str(num)

    # Check whether the number is equal to its reverse
    if value == value[::-1]:
        palindromes.append(num)

# Display the palindrome numbers
print("Palindrome Numbers:", palindromes)

