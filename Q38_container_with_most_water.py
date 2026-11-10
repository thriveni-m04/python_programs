# Q38. Container With Most Water
# Find two lines that can hold the maximum amount of water.

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(height) - 1

max_area = 0

while left < right:

    # Calculate width
    width = right - left

    # Water height is the shorter line
    h = min(height[left], height[right])

    # Calculate container area
    area = width * h

    # Update maximum area
    max_area = max(max_area, area)

    # Move the pointer with smaller height
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print("Maximum Water Area:", max_area)

# Expected Output:
# Maximum Water Area: 49