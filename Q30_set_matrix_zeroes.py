# Q30. Set Matrix Zeroes
# If an element is zero, make its entire row and column zero.
# The changes are made in the original matrix.

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

rows = len(matrix)
cols = len(matrix[0])

# Store the positions of all zero elements
zero_rows = set()
zero_cols = set()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

# Set the required rows and columns to zero
for i in range(rows):
    for j in range(cols):
        if i in zero_rows or j in zero_cols:
            matrix[i][j] = 0

print("Updated Matrix:")

for row in matrix:
    print(row)

# Expected Output:
# Updated Matrix:
# [1, 0, 1]
# [0, 0, 0]
# [1, 0, 1]
