
# Q45. Climbing Stairs

def climbing_stairs(n):
    patterns = []

    def generate(remaining, current):
        if remaining == 0:
            patterns.append("+".join(map(str, current)))
            return

        # Take one step
        if remaining >= 1:
            generate(remaining - 1, current + [1])

        # Take two steps
        if remaining >= 2:
            generate(remaining - 2, current + [2])

    generate(n, [])

    print("Total Ways:", len(patterns))
    print("Patterns:")

    for pattern in patterns:
        print(pattern)


# Sample input
n = 4

climbing_stairs(n)
