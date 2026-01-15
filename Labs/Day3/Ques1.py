# Question – Decorators

# Topic: Decorators

# Write a decorator called @execution_time that:

# 1. Measures the execution time of a function
# 2. Prints the function name and execution time
# 3. Apply this decorator to a function that calculates
# the factorial of a number using recursion


import time
from functools import wraps

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
        return result
    return wrapper


@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial:", factorial(5))
