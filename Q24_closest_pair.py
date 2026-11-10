# Q24. Closest Pair of Points
# Find the minimum distance between any two points.

import math

points = [(0, 0), (1, 1), (5, 5)]

minimum = float("inf")

# Compare every pair of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):

        x1, y1 = points[i]
        x2, y2 = points[j]

        # Calculate Euclidean distance
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if distance < minimum:
            minimum = distance

print("Closest Distance:", round(minimum, 2))
