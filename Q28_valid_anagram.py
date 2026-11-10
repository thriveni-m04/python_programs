# Q28. Valid Anagram
# Check whether two strings contain exactly the same characters.

s = input("Enter first string: ")
t = input("Enter second string: ")

# Sort both strings and compare them
if sorted(s) == sorted(t):
    print("Output: true")
else:
    print("Output: false")

# Sample Input:
# anagram
# nagaram
#
# Expected Output:
# Output: true