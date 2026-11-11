
# Q49. Cumulative Average Using a Closure

def calculate_average():
    numbers = []

    def add_number(num):
        numbers.append(num)

        # Calculate average of all entered numbers
        average = sum(numbers) / len(numbers)

        return average

    return add_number


# Create the closure function
average = calculate_average()

# Sample input
n = 4

for i in range(n):
    num = int(input("Enter number: "))
    print("Cumulative Average:", average(num))
