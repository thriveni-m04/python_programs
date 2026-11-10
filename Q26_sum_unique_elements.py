# Q26. Sum of Unique Elements
# Find elements that appear exactly once and calculate their sum.

numbers = [1, 3, 2, 3, 2, 4]

unique = []
total = 0

# Check how many times each element appears
for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)
        total += num

print("Original List:", numbers)

if len(unique) > 0:
    print("Unique Elements:", *unique)
else:
    print("Unique Elements: None")

print("Sum:", total)

