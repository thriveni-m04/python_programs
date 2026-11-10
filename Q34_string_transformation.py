# Q34. String Transformation with Given Substring
# Replace each character in the substring with its previous alphabet character.
# a becomes z, b becomes a, c becomes b, and so on.

s = input("Enter the original string: ")
sub = input("Enter the substring: ")

# Find the starting position of the substring
start = s.find(sub)

# Store transformed characters
new_sub = ""

for ch in sub:

    if ch == "a":
        new_sub += "z"
    else:
        new_sub += chr(ord(ch) - 1)

# Replace only the given substring
result = s[:start] + new_sub + s[start + len(sub):]

print("Updated String:", result)

# Sample Input:
# hackerrank
# hack
#
# Expected Output:
# Updated String: gzbjerrank