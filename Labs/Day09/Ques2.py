# Question 2 – Unit Testing & Test Driven Development (TDD)

# Topics Covered:
# Unit testing, Test Driven Development

# Implement Test Driven Development (TDD) for a simple calculator module.
# Requirements:
# 1. Write unit test cases first for operations:
# Addition
# Subtraction
# Multiplication
# Division

# 2. Use a Python unit testing framework (unittest or pytest)

# 3. Implement the calculator functions to make the tests pass

# 4. Demonstrate handling of edge cases (e.g., division by zero)

# 5. Explain the TDD cycle: Red → Green → Refactor







import pytest



# Part 1: Write unit test cases first for calculator operations

def test_addition():
    assert Calculator.add(2, 3) == 5


def test_subtraction():
    assert Calculator.subtract(5, 3) == 2


def test_multiplication():
    assert Calculator.multiply(4, 3) == 12


def test_division():
    assert Calculator.divide(10, 2) == 5



# Part 4: Demonstrate handling of edge cases (division by zero)

def test_division_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)



# Part 3: Implement the calculator functions to make tests pass

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b



# Part 5: Explain the TDD cycle (Red → Green → Refactor)

"""
Red:
Write tests first and see them fail.

Green:
Write minimum code to pass all tests.

Refactor:
Improve code without changing behavior.
"""



# Part 2: Use a Python unit testing framework

# Run tests using command: pytest

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************


# If you want to test  by UNIT Test




#
# import unittest
#
#
#
# # Part 1: Write unit test cases first for calculator operations
#
# class TestCalculator(unittest.TestCase):
#
#     def test_addition(self):
#         self.assertEqual(Calculator.add(2, 3), 5)
#
#     def test_subtraction(self):
#         self.assertEqual(Calculator.subtract(5, 3), 2)
#
#     def test_multiplication(self):
#         self.assertEqual(Calculator.multiply(4, 3), 12)
#
#     def test_division(self):
#         self.assertEqual(Calculator.divide(10, 2), 5)
#
#
#
# # Part 4: Demonstrate handling of edge cases (division by zero)
#
#     def test_division_by_zero(self):
#         with self.assertRaises(ValueError):
#             Calculator.divide(10, 0)
#
#
#
# # Part 3: Implement the calculator functions to make tests pass
#
# class Calculator:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def subtract(a, b):
#         return a - b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#     @staticmethod
#     def divide(a, b):
#         if b == 0:
#             raise ValueError("Division by zero is not allowed")
#         return a / b
#
#
#
# # Part 5: Explain the TDD cycle (Red → Green → Refactor)
#
# """
# Red:
# Write tests first and see them fail.
#
# Green:
# Write minimum code to pass all tests.
#
# Refactor:
# Improve code without changing behavior.
# """
#
#
#
# # Part 2: Use a Python unit testing framework
#
# if __name__ == "__main__":
#     unittest.main()
