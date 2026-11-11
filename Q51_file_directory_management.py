
# Q51. File and Directory Management Using os and time

import os
import time

# Create nested directories
folder = os.path.join("My_Project", "assignments", "task1")
os.makedirs(folder, exist_ok=True)

# Display current working directory
print("Current Working Directory:", os.getcwd())
print("Byte String Format:", os.getcwdb())

# Create and write a Python file
file_path = os.path.join(folder, "sample.py")

with open(file_path, "w") as file:
    file.write("print('Python Assignment')")

# Check whether directory exists
print(os.path.isdir(folder))

# Calculate total size of all files
total_size = 0

for root, directories, files in os.walk("My_Project"):
    for name in files:
        path = os.path.join(root, name)
        total_size += os.path.getsize(path)

print("total_size:", total_size, "bytes")

# Display file timestamps
print("access time:", time.ctime(os.path.getatime(file_path)))
print("Last modified time:", time.ctime(os.path.getmtime(file_path)))

# List directory contents
print("list of files in the directory:", os.listdir(folder))
