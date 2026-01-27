# Question 1 – Pytest Basics, Test Discovery & Assertions

# Topics Covered:
# Create a Pytest-based test suite for a simple Calculator module.
# Requirements:
# Pytest overview, Test discovery, Writing and running unit tests, Assert statements and exceptions

# 1. Write unit tests using Pytest conventions (test_*.py, test_ functions)

# 2. Demonstrate automatic test discovery

# 3. Use assert statements to validate results

# 4. Write a test to validate that an exception is raised for division by zero

# 5. Execute tests using the pytest command




# Calculator Module (Code Under Test)


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



# Pytest Unit Tests

# Part 1: Writing unit tests using Pytest conventions
#  File name starts with test_
#  Test functions start with test_

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5   # Part 3: assert statement


def test_subtraction():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6


def test_multiplication():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15


def test_division():
    calc = Calculator()
    assert calc.divide(20, 4) == 5



# Part 4: Test for Exception (Division by Zero)


import pytest

def test_division_by_zero_exception():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)



# Part 2: Automatic Test Discovery

# Pytest automatically discovers this file and all test_*
# functions when you run pytest from the terminal.



# Part 5: How to Execute Tests

# Run the following command in terminal:

#   pytest

