
# Q47. Sum of Odd Numbers in a List

nums = [1, 2, 3, 4, 5, 6]

# Approach 1: Using a regular function parameter
def sum_odd(numbers):
    total = 0

    for num in numbers:
        if num % 2 != 0:
            total += num

    return total


# Approach 2: Using list comprehension
odd_numbers = [num for num in nums if num % 2 != 0]
sum_using_list = sum(odd_numbers)


# Approach 3: Using a user-defined function
def odd_sum(numbers):
    return sum(num for num in numbers if num % 2 != 0)


print("Using Regular Function:", sum_odd(nums))
print("Using List Comprehension:", sum_using_list)
print("Using User-Defined Function:", odd_sum(nums))
