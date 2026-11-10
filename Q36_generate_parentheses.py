# Q36. Generate Parentheses
# Generate all possible valid combinations of n pairs of parentheses.

n = int(input("Enter number of pairs: "))

result = []

def generate(open_count, close_count, current):

    # If both counts reach n, save the combination
    if open_count == n and close_count == n:
        result.append(current)
        return

    # Add opening bracket if available
    if open_count < n:
        generate(open_count + 1, close_count, current + "(")

    # Add closing bracket only if valid
    if close_count < open_count:
        generate(open_count, close_count + 1, current + ")")


generate(0, 0, "")

print("Valid Parentheses:")
print(result)

