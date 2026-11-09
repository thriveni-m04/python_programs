# Question 8: Merge Triplets to Form Target Triplet
# Given a list of triplets and a target triplet,
# determine whether the target can be formed by merging
# suitable triplets using the maximum value of each position.

triplets = [
    [2, 5, 3],
    [1, 8, 4],
    [1, 7, 5]
]

target = [2, 7, 5]

# Track whether each target value has been obtained
found = [False, False, False]

# Examine every triplet
for triplet in triplets:

    # Ignore triplets that contain values greater than target
    if any(triplet[i] > target[i] for i in range(3)):
        continue

    # Check which target values this triplet contributes
    for i in range(3):

        if triplet[i] == target[i]:
            found[i] = True

# If all three values are found, target is possible
if all(found):
    print("Can Form Target:", True)
else:
    print("Can Form Target:", False)

