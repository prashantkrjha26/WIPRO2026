# Question 1 – Automation Framework Basics & Environment Setup

# Topics Covered:
# Introduction to automation frameworks in Python,
# Setting up the development environment

# Design a basic Python automation testing framework.
# Requirements:
# 1. Set up a virtual environment

# 2. Install required tools and libraries (e.g., pytest or unittest)

# 3. Create a project structure for an automation framework (tests, utilities, configuration)

# 4. Explain the role of:
# Test runner
# Test reports
# Configuration files

# 5. Write a sample test case to validate a simple function



# Part 1: Virtual Environment Creation
# A virtual environment is used to keep project dependencies separate
# from the system Python installation.
# It helps avoid version conflicts and makes the project easier to manage.

# Create Virtual Environment by >python -m venv venv_day9(name of environment)
# Activate   >.\venv_day9\Scripts\activate

# Part 2: Tools and Libraries
# pytest is used as the automation testing tool.
# It helps in writing test cases and executing them easily.
# pytest provides simple assertions and clear test results.

# Installation  >pytest
# Checking      >pytest --version


# Part 3: Project Structure for Automation Framework

# tests/
# Example test file:
def test_login():
    assert True

# utilities/
# Example utility function:
def add(a, b):
    return a + b
# This does not start with test_, so pytest treats it as normal code, not a test


# configuration/
# Example configuration values:
ENVIRONMENT = "QA"
TIMEOUT = 10
# Variables are never test items in pytest



# Part 4: Test Runner
# The test runner is responsible for discovering and executing test cases.
# pytest is used as the test runner in this framework.

import pytest

def test_sample():
    assert True


# Part 4: Test Reports
# Test reports show the result of test execution (pass or fail).
# pytest can generate reports such as HTML reports after running tests.


# Part 4: Configuration Files
# Configuration files store environment-specific values.
# These values help run the same tests in different environments.

ENVIRONMENT = "QA"
TIMEOUT = 10



# Part 5: Sample test case to validate a simple function

def add(a, b):
    return a + b

def test_add_function():
    assert add(2, 3) == 5


"""
Question 2 – Unit Testing & Test Driven Development (TDD)

Topics Covered:
Unit testing, Test Driven Development

This single Python file contains:
1. Unit test cases written first (TDD approach)
2. Calculator implementation to make tests pass
3. Edge case handling (division by zero)
4. Explanation of the TDD cycle (Red → Green → Refactor) using comments
"""

# ============================================================
# PART 1: IMPORT REQUIRED MODULES
# ============================================================
import unittest


# ============================================================
# PART 2: UNIT TESTS (Written FIRST as per TDD)
# ============================================================
class TestCalculator(unittest.TestCase):
    """
    These tests define the expected behavior of the calculator.
    In TDD, this step is called RED (tests fail because logic is not ready yet).
    """

    def test_addition(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(4, 3), 12)

    def test_division(self):
        self.assertEqual(Calculator.divide(10, 2), 5)

    def test_division_by_zero(self):
        """
        Edge case handling: division by zero
        The calculator should raise a ValueError
        """
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)


# ============================================================
# PART 3: CALCULATOR IMPLEMENTATION
# ============================================================
class Calculator:
    """
    This class is implemented AFTER writing tests.
    This step is called GREEN (write minimum code to pass tests).
    """

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


# ============================================================
# PART 4: TDD CYCLE EXPLANATION (RED → GREEN → REFACTOR)
# ============================================================
"""
RED:
- Write unit tests first.
- Run tests → they fail because calculator logic does not exist.

GREEN:
- Write the simplest possible code to make all tests pass.
- All tests should pass successfully.

REFACTOR:
- Improve code structure or readability without changing behavior.
- Example: using static methods, clean error handling.
"""


# ============================================================
# PART 5: RUN TESTS
# ============================================================
if __name__ == "__main__":
    unittest.main()

