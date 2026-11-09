# Q20. Word Break with All Segmentations
# Check whether a string can be divided into dictionary words.
# Print all possible valid segmentations.

s = "catsanddog"

wordDict = ["cat", "cats", "and", "sand", "dog"]

# Convert the dictionary into a set for faster searching.
word_set = set(wordDict)

# Store results for previously processed positions.
memo = {}


# Function to find all possible segmentations.
def word_break(start):

    # If the entire string is processed, return one empty combination.
    if start == len(s):
        return [[]]

    # Return previously calculated results.
    if start in memo:
        return memo[start]

    results = []

    # Try different ending positions.
    for end in range(start + 1, len(s) + 1):

        # Extract a possible word.
        word = s[start:end]

        # Check whether the word exists in the dictionary.
        if word in word_set:

            # Find segmentations for the remaining string.
            remaining = word_break(end)

            # Add the current word to every valid segmentation.
            for combination in remaining:
                results.append([word] + combination)

    # Store the results for this position.
    memo[start] = results

    return results


# Find all possible segmentations.
segmentations = word_break(0)

if segmentations:

    print("Can Segment: True")

    print("Segmentations:")

    for combination in segmentations:
        print(" ".join(combination))

else:

    print("Can Segment: False")
    print("Segmentations: None")
    