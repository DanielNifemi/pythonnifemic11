import functools
import time
from functools import wraps


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.2E} seconds")
        return value

    return wrapper


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print("About to be decorated")
        value = func(*args, **kwargs)
        print("Just Decorated")
        return value

    return wrapper


@print_decorator
def printer():
    return "I am a printer"


@timer
@print_decorator
def factorial(num: int) -> int:
    """
    Calculates the factorial of a number
    :param num: The number to calculate the factorial of
    :return: The factorial of the number
    """
    import math
    return math.factorial(num)

@timer
def my_factorial(num):
    product = 1
    for i in range(0, -1, num):
        product *= i
    return product


# printer = print_decorator(printer)
# print(printer())

print(factorial(5))
print(my_factorial(5))
