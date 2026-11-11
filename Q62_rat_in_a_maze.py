
# Q62: Rat in a Maze Using Backtracking

def solve_maze(maze):

    n = len(maze)

    # Create an empty solution matrix
    solution = [[0 for j in range(n)] for i in range(n)]

    # Check whether a cell is safe
    def is_safe(row, col):

        return (
            0 <= row < n and
            0 <= col < n and
            maze[row][col] == 1 and
            solution[row][col] == 0
        )

    # Recursive function
    def find_path(row, col):

        # Destination reached
        if row == n - 1 and col == n - 1:
            solution[row][col] = 1
            return True

        if is_safe(row, col):

            # Mark current cell as part of path
            solution[row][col] = 1

            # Four possible directions
            directions = [
                (1, 0),    # Down
                (-1, 0),   # Up
                (0, 1),    # Right
                (0, -1)    # Left
            ]

            for dr, dc in directions:

                if find_path(row + dr, col + dc):
                    return True

            # Backtrack if no path is found
            solution[row][col] = 0

        return False

    if find_path(0, 0):

        print("Solution Path:")

        for row in solution:
            print("".join(map(str, row)))

    else:
        print("No solution exists")


# Example 1
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
