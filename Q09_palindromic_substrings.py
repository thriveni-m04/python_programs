# Question 9: Palindromic Substrings with Pattern Listing
# Given a lowercase string, count all palindromic substrings.
# Also print every palindrome.
# Duplicate substrings at different positions must be counted
# separately.

s = "ababa"

palindromes = []


# Function to expand around the given center
def find_palindromes(left, right):

    while left >= 0 and right < len(s):

        # Check whether characters are equal
        if s[left] == s[right]:

            # Store the palindrome substring
            palindromes.append(s[left:right + 1])

            # Expand towards both sides
            left -= 1
            right += 1

        else:
            break


# Check every possible center
for i in range(len(s)):

    # Odd-length palindromes
    find_palindromes(i, i)

    # Even-length palindromes
    find_palindromes(i, i + 1)


# Display total count
print("Total Count:", len(palindromes))

print("Palindromic Substrings:")

for word in palindromes:
    print(word)

