# Question 2 – Setup/Teardown, Fixtures & conftest.py

# Topics Covered:
# xUnit style setup and teardown, Test fixtures, conftest.py

# Enhance the test suite created in Question 1.
# Requirements:

# 1. Implement xUnit-style methods (setup_module, teardown_module, setup_function, teardown_function)

# 2. Create reusable fixtures for test data and resources

# 3. Move common fixtures to a conftest.py file

# 4. Demonstrate fixture scope (function, module)

# 5. Use fixtures in multiple test file




import pytest


# Calculator Module (from Question 1)


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b



# Part 1: xUnit-Style Setup and Teardown (Module Level)


def setup_module(module):
    print("\n[setup_module] Runs once before all tests in this module")


def teardown_module(module):
    print("\n[teardown_module] Runs once after all tests in this module")



# Part 1: xUnit-Style Setup and Teardown (Function Level)


def setup_function(function):
    print(f"\n[setup_function] Runs before {function.__name__}")


def teardown_function(function):
    print(f"\n[teardown_function] Runs after {function.__name__}")



# Part 2 & 4: Pytest Fixtures with Scope


#  Function scoped fixture (default) 
@pytest.fixture(scope="function")
def calculator():
    print("[fixture: calculator] Function scope")
    return Calculator()


#  Module scoped fixture 
@pytest.fixture(scope="module")
def test_numbers():
    print("[fixture: test_numbers] Module scope")
    return (10, 5)



# Part 3: conftest.py Explanation

"""
In real projects, shared fixtures like 'calculator' and 'test_numbers'
should be moved into a separate file named: conftest.py

Pytest automatically discovers conftest.py and makes its fixtures
available to all test files without importing them.

For this assignment, everything is kept in one file"""



# Part 5: Using Fixtures in Multiple Test Functions
# (Simulating multiple test files)


def test_addition(calculator, test_numbers):
    a, b = test_numbers
    assert calculator.add(a, b) == 15


def test_subtraction(calculator, test_numbers):
    a, b = test_numbers
    assert calculator.subtract(a, b) == 5


def test_multiplication(calculator):
    assert calculator.multiply(3, 4) == 12


def test_division(calculator):
    assert calculator.divide(20, 4) == 5


def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)



# How to Run

"""
Run from terminal:

    pytest 

Observe:
- setup_module / teardown_module run once
- setup_function / teardown_function run for every test
- function-scoped fixture runs every test
- module-scoped fixture runs once per module
"""
