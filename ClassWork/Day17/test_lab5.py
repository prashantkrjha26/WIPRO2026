# Test Scenario: Register Account – TutorialsNinja Demo
# Base URL: https://tutorialsninja.com/demo/
# Pre-condition:
# All variables should be defined before they are used.

# Part 1: Launch Application
# Launch the application using Microsoft Edge browser.
# Navigate to the given URL.
# Verify the title of the home page.
# Click on the My Account dropdown.
# Select Register from the dropdown.
# Verify that the Register Account page is displayed by checking the heading “Register Account”.
# Click on the Continue button without entering any details.
# Verify the warning message:
# “Warning: You must agree to the Privacy Policy!”

# Part 2: Your Personal Details
# Enter data in the First Name text box.
# Enter 33 characters in the First Name field and click Continue.
# Verify that only 32 characters are allowed.
# If not allowed, verify the error message displayed.
# Enter data in the Last Name text box.
# Enter 33 characters in the Last Name field and click Continue.
# Verify that only 32 characters are allowed.
# If not allowed, verify the error message displayed.
# Enter a valid E-mail address.
# Enter a Telephone number containing between 3 and 32 characters.

# Part 3: Your Address
# Enter Address 1 with characters between 3 and 128.
# Enter City with characters between 2 and 128.
# Enter Post Code with characters between 2 and 10.
# Select India from the Country dropdown.
# Select a value from the Region / State dropdown.

# Part 4: Password
# Enter a Password with characters between 4 and 20.
# Enter the same value in the Password Confirm field.
# Part 5: Newsletter and Privacy Policy
# Select Yes for the Newsletter option.
# Select the checkbox “I have read and agree to the Privacy Policy”.
# Click on the Continue button.
# Verify the success message:
# “Your Account Has Been Created!”
# Click on Continue.
# Under My Orders, click on View your order history.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_account():

    # Base URL and test data (variables defined before use)
    base_url = "https://tutorialsninja.com/demo/"
    first_name_33 = "A" * 33              # Creates 33 characters for validation
    last_name_33 = "B" * 33               # Creates 33 characters for validation
    valid_first_name = "Prashant"         # Valid first name
    valid_last_name = "Jha"               # Valid last name
    email = f"testuser{int(time.time())}@mail.com"  # Generates unique email
    telephone = "9876543210"              # Valid telephone number
    password = "test1234"                 # Valid password (4–20 chars)

    driver = webdriver.Edge()             # Launches Edge browser
    wait = WebDriverWait(driver, 15)       # Applies explicit wait
    driver.maximize_window()               # Maximizes browser window
    driver.get(base_url)                   # Navigates to application URL

    def type_field(locator, value):
        field = wait.until(EC.visibility_of_element_located(locator))  # Waits for field visibility
        field.clear()                          # Clears existing text
        field.send_keys(value)                # Enters required value

    assert "Your Store" in driver.title     # Verifies title of home page

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()  # Opens My Account dropdown
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()  # Clicks Register option

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h1[text()='Register Account']")))  # Verifies Register Account page heading

    driver.find_element(By.XPATH, "//input[@value='Continue']").click()  # Clicks Continue without data

    warning = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "alert-danger")))    # Captures privacy policy warning
    assert "Privacy Policy" in warning.text  # Verifies warning message text

    type_field((By.ID, "input-firstname"), first_name_33)  # Enters 33 chars in First Name
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()  # Clicks Continue to validate

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[text()='First Name must be between 1 and 32 characters!']")))  # Verifies error

    type_field((By.ID, "input-firstname"), valid_first_name)  # Enters valid First Name

    type_field((By.ID, "input-lastname"), last_name_33)  # Enters 33 chars in Last Name
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()  # Clicks Continue to validate

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[text()='Last Name must be between 1 and 32 characters!']")))  # Verifies error

    type_field((By.ID, "input-lastname"), valid_last_name)  # Enters valid Last Name

    type_field((By.ID, "input-email"), email)        # Enters valid email address
    type_field((By.ID, "input-telephone"), telephone)  # Enters valid telephone number

    type_field((By.ID, "input-password"), password)  # Enters password
    type_field((By.ID, "input-confirm"), password)   # Confirms password

    driver.find_element(By.XPATH,
        "//input[@name='newsletter' and @value='1']").click()  # Selects Newsletter = Yes
    driver.find_element(By.NAME, "agree").click()     # Accepts Privacy Policy checkbox

    driver.find_element(By.XPATH, "//input[@value='Continue']").click()  # Submits registration form

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h1[text()='Your Account Has Been Created!']")))  # Verifies success message

    driver.find_element(By.LINK_TEXT, "Continue").click()  # Clicks Continue after account creation

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()  # Opens My Account menu
    driver.find_element(By.LINK_TEXT, "Order History").click()  # Opens View Order History

    time.sleep(5)                    # Holds browser for visibility
    driver.quit()                    # Closes browser
