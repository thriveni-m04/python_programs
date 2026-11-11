
# Q44. Rotate Image

def rotate_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for row in matrix:
        row.reverse()

    return matrix


# Sample input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Rotated Matrix:")
for row in rotate_matrix(matrix):
    print(row)
