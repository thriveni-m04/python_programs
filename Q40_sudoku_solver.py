# Q40. Validate and Complete a 9x9 Sudoku Board
# First check whether the given Sudoku is valid.
# If valid, solve it using backtracking.

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


# Validate the existing filled cells
def validate(board):

    # Check all 3x3 boxes first
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):

            seen = set()

            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):

                    value = board[i][j]

                    if value != ".":
                        if value in seen:
                            return False, "Duplicate found in a 3x3 box"

                        seen.add(value)

    # Check every row
    for row in board:
        values = [x for x in row if x != "."]

        if len(values) != len(set(values)):
            return False, "Duplicate found in a row"

    # Check every column
    for col in range(9):

        values = [
            board[row][col]
            for row in range(9)
            if board[row][col] != "."
        ]

        if len(values) != len(set(values)):
            return False, "Duplicate found in a column"

    return True, "Sudoku is valid"


# Check whether a number can be placed
def is_safe(board, row, col, num):

    # Check the row and column
    for i in range(9):
        if board[row][i] == num:
            return False

        if board[i][col] == num:
            return False

    # Find the starting position of the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check the 3x3 box
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# Solve Sudoku using backtracking
def solve(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == ".":

                for num in "123456789":

                    if is_safe(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        # Undo the number if it leads to no solution
                        board[row][col] = "."

                return False

    return True


# Main program
valid, message = validate(board)

print("Valid Sudoku:", valid)

if valid:

    if solve(board):

        print("Completed Sudoku:")

        for i in range(9):

            print(" ".join(board[i][0:3]), end=" | ")
            print(" ".join(board[i][3:6]), end=" | ")
            print(" ".join(board[i][6:9]))

            if i == 2 or i == 5:
                print("---------------------------")

else:
    print("Reason:", message)

