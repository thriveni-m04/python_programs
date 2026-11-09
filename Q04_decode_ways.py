# Question 4: Decode Ways with Pattern Generation
# Given a string containing digits, decode it using the mapping
# 1 = A, 2 = B, ..., 26 = Z.
# Print the total number of valid decoding ways and all
# possible decoded strings.
# No segment can start with zero.

s = "226"

decoded_strings = []

def decode(index, current):

    # If all digits are processed, store the decoded string
    if index == len(s):
        decoded_strings.append(current)
        return

    # A number cannot start with zero
    if s[index] == '0':
        return

    # Decode one digit
    num = int(s[index])
    letter = chr(64 + num)

    decode(index + 1, current + letter)

    # Decode two digits if they form a number from 10 to 26
    if index + 1 < len(s):

        num = int(s[index:index + 2])

        if 10 <= num <= 26:
            letter = chr(64 + num)

            decode(index + 2, current + letter)


# Start decoding from index 0
decode(0, "")

# Display total number of ways
print("Total Ways:", len(decoded_strings))

print("Decoded Strings:")

if decoded_strings:
    for word in decoded_strings:
        print(word)
else:
    print("None")

