
# Q60. Insert Sensor Reading into NumPy Array

import numpy as np

# Original sensor readings
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

try:
    # Get insertion position
    position = int(input("Enter insertion position: "))

    # Get new sensor reading
    element = input("Enter new sensor reading: ")

    # Check whether input contains only digits
    if not element.isdigit():
        raise ValueError("Only integer values are allowed.")

    # Check whether position is valid
    if position < 0 or position > len(arr):
        raise IndexError("Invalid insertion position.")

    # Convert input into integer
    element = int(element)

    # Insert new value
    arr = np.insert(arr, position, element)

    print("Updated Array:", arr)

except ValueError as error:
    print("Value Error:", error)

except IndexError as error:
    print("Index Error:", error)

finally:
    print("Insertion operation completed.")

