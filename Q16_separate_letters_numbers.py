# Q16. Separate Letters and Numbers from a String
# Extract letters and digits separately while maintaining their order.

s = "a1b2c3d4"

letters = ""
digits = ""

# Check every character in the string.
for char in s:

    # Check whether the character is an alphabet.
    if char.isalpha():
        letters += char

    # Check whether the character is a digit.
    elif char.isdigit():
        digits += char

# Store both strings in a list.
result = [letters, digits]

print("Result:", result)