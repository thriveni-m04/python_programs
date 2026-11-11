
# Q57. Student Performance Analyzer

import random
from datetime import date
from collections import Counter
from functools import reduce

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

averages = {}

# Calculate each student's average
for name, marks in students.items():
    averages[name] = sum(marks) / len(marks)

    print(name, "Average:", round(averages[name], 2))

# Find highest average
top_student = max(averages, key=averages.get)

print("Highest Average:", top_student, averages[top_student])

# Randomly select one student
selected = random.choice(list(students.keys()))
print("Randomly Selected Student:", selected)

# Display current date
print("Current Date:", date.today())

# Classify grades using Counter
grades = []

for average in averages.values():
    if average >= 90:
        grades.append("A")
    elif average >= 75:
        grades.append("B")
    elif average >= 60:
        grades.append("C")
    else:
        grades.append("D")

grade_count = Counter(grades)

print("Grade Classification:", grade_count)

# Calculate total marks using reduce()
all_marks = []

for marks in students.values():
    all_marks.extend(marks)

total = reduce(lambda a, b: a + b, all_marks)

print("Total Marks:", total)
