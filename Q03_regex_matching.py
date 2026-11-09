# Question 3: Regular Expression Matching
# Given a string s and a pattern p, implement regular expression
# matching with support for '.' and '*'.
# '.' matches any single character.
# '*' matches zero or more of the preceding character.
# The pattern must match the entire string.

s = "abcd"
p = ".*"

# Create a DP table
# dp[i][j] means the first i characters of s
# match the first j characters of p.

rows = len(s) + 1
cols = len(p) + 1

dp = [[False] * cols for _ in range(rows)]

# Empty string matches empty pattern
dp[0][0] = True

# Handle patterns such as a*, a*b*
for j in range(2, cols):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

# Fill the DP table
for i in range(1, rows):
    for j in range(1, cols):

        # If characters match or pattern contains '.'
        if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        # If pattern contains '*'
        elif p[j - 1] == '*':

            # Consider zero occurrences of previous character
            dp[i][j] = dp[i][j - 2]

            # Consider one or more occurrences
            if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]

# Display the result
print("Matching Result:", dp[len(s)][len(p)])
