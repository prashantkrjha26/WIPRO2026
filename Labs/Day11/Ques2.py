# Question 4 – Parallel Execution, Reporting & Functional Testing

# Topics Covered:
# Distributed and parallel tests, Reporting test results
# and tracking test history, Writing functional tests

# Design a functional test suite using Pytest.

# Requirements:
# 1. Write functional tests that test end-to-end behavior

# 2. Execute tests in parallel using pytest-xdist

# 3. Generate test reports:
# HTML report
# JUnit XML report

# 4. Maintain and analyze test execution history

# 5. Explain how Pytest supports scalable test automation


"""
Question 4 – Parallel Execution, Reporting & Functional Testing
"""

import pytest


# Question Part 1:
# Write functional tests that test end-to-end behavior


class TestLoginFlow:

    def test_valid_login(self):
        assert login("Admin", "admin123") == "Login Successful"

    def test_invalid_login(self):
        assert login("Admin", "wrongpass") == "Login Failed"

    def test_empty_credentials(self):
        assert login("", "") == "Login Failed"


def login(username, password):
    if username == "Admin" and password == "admin123":
        return "Login Successful"
    return "Login Failed"



# Question Part 2:
# Execute tests in parallel using pytest-xdist

# Command:
# pip install pytest-xdist
# pytest -n 3 Ques2.py



# Question Part 3:
# Generate test reports (HTML and JUnit XML)

# Command:
# pip install pytest-html
# pytest -n 3 Ques2.py --html=report_Ques2.html --self-contained-html
# pytest -n 3 Ques2.py --junitxml=report_Ques2.xml



# Question Part 4:
# Maintain and analyze test execution history

# Command:
# pytest Ques2.py --lf



# Question Part 5:
# Explain how Pytest supports scalable test automation

# Pytest supports scalability using parallel execution, plugins,
# test discovery, reporting, and execution history.

