
# Q56. Move All Zeros to the End

l = [0, 1, 0, 2, 0, 3]

# Extract non-zero elements
non_zeros = [num for num in l if num != 0]

# Extract zero elements
zeros = [num for num in l if num == 0]

# Combine both lists
result = non_zeros + zeros

print(result)
