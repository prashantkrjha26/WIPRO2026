# Question 3 – Parameterization, CLI Options, Skips & Expected Failures

# Topics Covered:
# Parameterizing tests, Pytest command line arguments, Customizing tests
# with CLI/config files, Handling skips and expected failures

# Extend the Pytest framework to include advanced test controls.

# Requirements:
# 1. Use @pytest.mark.parametrize to test multiple input combinations

# 2. Create a custom command-line option using pytest_addoption

# 3. Read configuration values from pytest.ini

# 4. Mark certain tests as:
# skip
# xfail

# 5. Execute tests with different command-line options





import pytest


# Question Part 2:
# Create a custom command-line option using pytest_addoption


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests: dev / qa / prod"
    )



# Question Part 3:
# Read configuration values from pytest.ini (SAFE fallback)


@pytest.fixture
def app_name(pytestconfig):
    try:
        return pytestconfig.getini("app_name")
    except ValueError:
        # Fallback if pytest.ini is not present
        return "SampleApp"



# Question Part 1:
# Parameterized test cases


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5),
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected



# Question Part 4:
# Skip test


@pytest.mark.skip(reason="Feature under development")
def test_future_feature():
    assert True



# Question Part 4:
# Expected failure (xfail)


@pytest.mark.xfail(reason="Known bug: division by zero not handled")
def test_division_by_zero():
    result = 10 / 0
    assert result == 0



# Question Part 5:
# Execute tests with different command-line options


def test_environment_option(request):
    env = request.config.getoption("env", default="dev")
    assert env in ["dev", "qa", "prod"]



# Using config value (from ini or fallback)


def test_app_name_from_ini(app_name):
    assert isinstance(app_name, str)
    assert len(app_name) > 0
