# Q29. Happy Number
# Check whether repeated sums of squared digits eventually become 1.

n = int(input("Enter a number: "))

seen = set()

while n != 1 and n not in seen:

    # Store the number to detect a repeating cycle
    seen.add(n)

    total = 0

    # Calculate the sum of squares of digits
    for digit in str(n):
        total += int(digit) ** 2

    n = total

if n == 1:
    print("Output: true")
else:
    print("Output: false")

# Sample Input: 19
# Expected Output:
# Output: true