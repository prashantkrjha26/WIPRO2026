# 7 – Automation Framework (POM)

# Write a Selenium automation framework that:
# 1. Implements Page Object Model (POM)
# 2. Separates page classes, test scripts, and configuration
# 3. Creates reusable methods for common actions (click, input, select)
# 4. Runs a test using pytest or unittest and prints results




# Part 1: Implement Page Object Model (POM)
# Part 2: Separate page logic, test logic, and configuration (done logically in one file)

from selenium import webdriver                      # Imports Edge browser control
from selenium.webdriver.common.by import By         # Provides locator strategies
from selenium.webdriver.support.ui import WebDriverWait  # Enables explicit waiting
from selenium.webdriver.support import expected_conditions as EC  # Defines wait conditions
import pytest                                       # Enables pytest framework

# Part 2: Configuration details
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"  # OrangeHRM URL
USERNAME = "Admin"                                  # OrangeHRM demo username
PASSWORD = "admin123"                               # OrangeHRM demo password

# Part 3: Reusable methods for common actions
class BasePage:
    def __init__(self, driver):
        self.driver = driver                          # Holds browser instance
        self.wait = WebDriverWait(driver, 10)         # Waits for elements

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()  # Clicks element

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))  # Finds element
        element.clear()                               # Clears input field
        element.send_keys(text)                       # Types text into field

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text  # Reads text

# Part 1: Page Object Model implementation
class LoginPage(BasePage):
    username_input = (By.NAME, "username")           # Locator for username field
    password_input = (By.NAME, "password")           # Locator for password field
    login_button = (By.XPATH, "//button[@type='submit']")  # Locator for login button
    dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")  # Locator for dashboard heading

    def login(self, username, password):
        self.enter_text(self.username_input, username)  # Enters username
        self.enter_text(self.password_input, password)  # Enters password
        self.click(self.login_button)                   # Clicks login button

    def get_dashboard_text(self):
        return self.get_text(self.dashboard_text)       # Gets dashboard text

# Part 4: Run test using pytest and print result
@pytest.fixture
def setup():
    driver = webdriver.Edge()                         # Launches Edge browser
    driver.maximize_window()                          # Maximizes browser window
    driver.get(BASE_URL)                              # Opens OrangeHRM login page
    yield driver                                      # Provides driver to test
    driver.quit()                                     # Closes browser

# Part 4: Test script execution
def test_valid_login(setup):
    login_page = LoginPage(setup)                     # Creates LoginPage object
    login_page.login(USERNAME, PASSWORD)              # Performs login action

    dashboard = login_page.get_dashboard_text()       # Captures dashboard heading
    print("Login Result:", dashboard)                 # Prints test result

    assert "Dashboard" in dashboard                   # Validates successful login
