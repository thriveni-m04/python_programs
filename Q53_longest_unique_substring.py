
# Q53. Longest Substring Without Repeating Characters

def longest_unique_substring(s):
    visited = [False] * 26

    left = 0
    maximum = 0

    for right in range(len(s)):
        index = ord(s[right]) - ord('a')

        # Remove repeated characters from the left
        while visited[index]:
            left_index = ord(s[left]) - ord('a')
            visited[left_index] = False
            left += 1

        # Mark current character as visited
        visited[index] = True

        # Update maximum length
        maximum = max(maximum, right - left + 1)

    return maximum


# Sample input
s = "abcabcbb"

print("Length of the longest unique substring:", longest_unique_substring(s))
