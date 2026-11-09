# Question 7: Minimize Maximum Consecutive Zeros
# Given L (length of binary string) and K (number of ones):
# 1. Generate all possible binary strings of length L
#    containing exactly K ones.
# 2. Find the longest consecutive block of zeros in each string.
# 3. Print the arrangements that minimize this maximum block.

from itertools import combinations

L = 4
K = 2

possible_strings = []
minimum_zero_block = L + 1
optimal_strings = []


# Function to calculate maximum consecutive zeros
def max_zeros(binary_string):

    count = 0
    maximum = 0

    for bit in binary_string:

        if bit == '0':
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


# Generate all positions where ones can be placed
for positions in combinations(range(L), K):

    # Initially create a string containing only zeros
    binary_list = ['0'] * L

    # Place ones at the selected positions
    for position in positions:
        binary_list[position] = '1'

    # Convert list into a binary string
    binary_string = ''.join(binary_list)

    # Calculate maximum consecutive zeros
    zero_count = max_zeros(binary_string)

    possible_strings.append((binary_string, zero_count))

    # Find the minimum maximum-zero block
    if zero_count < minimum_zero_block:
        minimum_zero_block = zero_count
        optimal_strings = [binary_string]

    elif zero_count == minimum_zero_block:
        optimal_strings.append(binary_string)


# Display all possible strings
print("Possible Strings:")

for binary_string, zero_count in possible_strings:
    print(binary_string, "-> max zeros =", zero_count)

# Display optimal arrangements
print("Optimal Arrangements:", optimal_strings)

print("Minimum Longest Zero Block:", minimum_zero_block)

