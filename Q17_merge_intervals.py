# Q17. Merge Intervals
# Merge all overlapping intervals.

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Sort intervals according to their starting values.
intervals.sort()

# Store the merged intervals.
merged = []

for interval in intervals:

    # If the list is empty, add the first interval.
    if not merged:

        merged.append(interval)

    # Check whether the current interval overlaps with the previous one.
    elif interval[0] <= merged[-1][1]:

        # Update the ending value if necessary.
        merged[-1][1] = max(merged[-1][1], interval[1])

    else:

        # No overlap, so add a new interval.
        merged.append(interval)

print("Merged Intervals:", merged)