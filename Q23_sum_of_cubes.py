# Q23. Sum of Cubes in a Given Range
# Calculate the sum of cubes from a to b (inclusive).

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

total = 0

# Calculate cube of each number and add it
for i in range(a, b + 1):
    total = total + (i ** 3)

print("Sum of Cubes:", total)

# Sample Input:
# 4
# 9
#
# Expected Output:
# Sum of Cubes: 1989