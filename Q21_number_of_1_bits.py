# Q21. Number of 1 Bits
# Count the number of set bits (1s) in the binary representation.

n = int(input("Enter a positive number: "))

# Convert the number into binary and count the 1s
binary = bin(n)[2:]
count = binary.count("1")

print("Binary Representation:", binary)
print("Number of 1 Bits:", count)

