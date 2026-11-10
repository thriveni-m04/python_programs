# Q32. Toggle K-th Bit
# Toggle means changing 0 to 1 or 1 to 0.

n = int(input("Enter a number: "))
k = int(input("Enter bit position: "))

# Create a mask with 1 at the kth position
mask = 1 << k

# XOR toggles the selected bit
result = n ^ mask

print("Result:", result)

# Sample Input:
# n = 5
# k = 1
#
# Expected Output:
# Result: 7
