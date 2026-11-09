# Q15. Reverse Bits
# Reverse all 32 bits of a given integer.

n = 43261596

result = 0

# Process exactly 32 bits.
for i in range(32):

    # Extract the last bit of n.
    bit = n & 1

    # Shift the result left by one position.
    result = (result << 1) | bit

    # Shift n right to process the next bit.
    n = n >> 1

print("Reversed Bits:", result)
