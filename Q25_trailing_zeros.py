# Q25. Count Trailing Zeros in Binary
# Count the zeros present at the right end of binary representation.

n = int(input("Enter a number: "))

binary = bin(n)[2:]

# Count zeros from the right side
count = 0

for digit in reversed(binary):
    if digit == "0":
        count += 1
    else:
        break

print("Binary Representation:", binary)
print("Trailing Zeros:", count)

