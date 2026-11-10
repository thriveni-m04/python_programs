# Q39. Matrix Chain Multiplication
# Find the minimum multiplication cost and optimal order.

# Matrix dimensions
# A1 = 10 x 30
# A2 = 30 x 5
# A3 = 5 x 60

p = [10, 30, 5, 60]

n = len(p) - 1

# Create DP tables
dp = [[0] * n for _ in range(n)]
split = [[0] * n for _ in range(n)]

# Calculate minimum multiplication cost
for length in range(2, n + 1):

    for i in range(n - length + 1):

        j = i + length - 1
        dp[i][j] = float("inf")

        for k in range(i, j):

            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + p[i] * p[k + 1] * p[j + 1]
            )

            if cost < dp[i][j]:
                dp[i][j] = cost
                split[i][j] = k


# Build the parenthesization and multiplication steps
steps = []

def build_order(i, j):

    # A single matrix needs no multiplication
    if i == j:
        return "A" + str(i + 1)

    k = split[i][j]

    left = build_order(i, k)
    right = build_order(k + 1, j)

    expression = "(" + left + " x " + right + ")"

    # Store each multiplication after its subproblems
    steps.append(expression)

    return expression


order = build_order(0, n - 1)

print("Minimum Cost:", dp[0][n - 1])
print("Optimal Parenthesization:", order)

print("Multiplication Sequence:")

for i in range(len(steps)):
    print("Step", i + 1, ":", steps[i])

