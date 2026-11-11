
# Q50. Remove Elements Greater Than 20 Using Decorator and Filter

def filter_decorator(func):
    def wrapper(nums):
        # Keep only numbers less than or equal to 20
        result = list(filter(lambda x: x <= 20, nums))
        return func(result)

    return wrapper


@filter_decorator
def display_list(nums):
    return nums


# Sample input
nums = [5, 10, 23, 40, 8]

print("Filtered List:", display_list(nums))
