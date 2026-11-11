
# Q52. CSV Data Cleaning and JSON File Conversion

import csv
import json

# Store CSV data as a multiline string
raw_data = """Name,Age,Salary,Join Date
Alice, 30, 95000, 2015-03-01
Bob, , 60000, 2018-07-15
Charlie, 35, Unknown, 2024-02-01
Diana, 40, 110000, 2021-11-03"""

# Separate data into lines
lines = raw_data.splitlines()

# Read CSV records
reader = csv.DictReader(lines)

cleaned_records = []

for row in reader:
    # Remove extra spaces
    row = {key: value.strip() for key, value in row.items()}

    # Skip missing or invalid values
    if not row["Age"] or not row["Salary"]:
        continue

    if row["Salary"].lower() == "unknown":
        continue

    try:
        age = int(row["Age"])
        salary = float(row["Salary"])

        # Create a clean employee record
        employee = {
            "name": row["Name"],
            "age": age,
            "salary": salary,
            "join_date": row["Join Date"]
        }

        cleaned_records.append(employee)

    except ValueError:
        print("Skipping invalid record:", row["Name"])

# Save cleaned records to JSON file
with open("cleaned_data.json", "w") as file:
    json.dump(cleaned_records, file, indent=2)

print("Cleaned records:")
print(json.dumps(cleaned_records, indent=2))
print("Data saved to cleaned_data.json")
