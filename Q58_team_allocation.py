
# Q58. Automated Course Project Team Allocation

import sys
import random
import math
from collections import defaultdict
from itertools import combinations
from functools import reduce
from datetime import date

# Sample student details: name, department, marks
students = [
    ("Anita", "CSE", 85),
    ("Rahul", "CSE", 78),
    ("Priya", "CSE", 92),
    ("Kiran", "CSE", 80),

    ("Arun", "AI", 88),
    ("Meena", "AI", 90),
    ("Ravi", "AI", 76),
    ("Divya", "AI", 84),

    ("Sneha", "Data Science", 91),
    ("Ajay", "Data Science", 82),
    ("Neha", "Data Science", 79),
    ("Vijay", "Data Science", 86)
]

# Read team size from command line
if len(sys.argv) > 1:
    team_size = int(sys.argv[1])
else:
    team_size = 3

# Group students by department
departments = defaultdict(list)

for student in students:
    departments[student[1]].append(student)

# Display heading
print("===== PROJECT TEAM ALLOCATION =====")
print("Team Size:", team_size)
print("Allocation Date:", date.today().strftime("%d-%m-%Y"))

# Select a department with enough students
available = [
    dept for dept, members in departments.items()
    if len(members) >= team_size
]

if team_size <= 0 or not available:
    print("No team can be created with this team size.")
else:
    department = random.choice(available)
    members = departments[department]

    # Generate possible team combinations
    possible_teams = list(combinations(members, team_size))

    # Randomly select one team
    selected_team = random.choice(possible_teams)

    print("Department:", department)
    print("Selected Team:")

    marks = []

    for i, student in enumerate(selected_team, 1):
        print(i, student[0], "-", student[2])
        marks.append(student[2])

    # Calculate total marks using reduce
    total = reduce(lambda a, b: a + b, marks)

    average = total / team_size

    print("Total Marks:", total)
    print("Average Marks:", format(average, ".2f"))
