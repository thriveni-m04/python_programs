
# Q48. Palindrome Number Using a Decorator

def check_palindrome(func):
    def wrapper(num):
        result = func(num)

        if result:
            print(num, "is a Palindrome")
        else:
            print(num, "is Not a Palindrome")

    return wrapper


@check_palindrome
def is_palindrome(num):
    # Reverse the number using string slicing
    return str(num) == str(num)[::-1]


# Sample input
num = 121

is_palindrome(num)
