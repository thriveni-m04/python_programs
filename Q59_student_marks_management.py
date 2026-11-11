
# Q59. Student Marks Management System

class InvalidMarksError(Exception):
    pass


while True:
    try:
        name = input("Enter student name: ")

        # Check that name is not empty
        assert name.strip() != "", "Student name cannot be empty"

        marks = float(input("Enter student marks: "))

        # Check marks range
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")

        # Save valid record
        with open("student_records.txt", "a") as file:
            file.write(name + " - " + str(marks) + "\n")

        print("Record saved successfully!")

    except ValueError:
        print("Error: Please enter numeric marks.")

    except InvalidMarksError as error:
        print("Error:", error)

    except AssertionError as error:
        print("Error:", error)

    finally:
        print("Record processing completed.")

    choice = input("Do you want to enter another record? (yes/no): ")

    if choice.lower() != "yes":
        break
