# Question 5 – Handling Web Controls

# Write a Selenium script that:
# 1. Fills text boxes
# 2. Selects radio buttons and checkboxes
# 3. Chooses an option from a drop-down list using the Select class
# 4. Submits the form and verifies a confirmation message

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1. Fills text boxes
driver.find_element(By.NAME, "my-text").send_keys("Prashant")        # Enters text in Text input field
driver.find_element(By.NAME, "my-password").send_keys("Test@123")   # Enters value in Password field
driver.find_element(By.NAME, "my-textarea").send_keys("India")      # Enters text in Textarea field
time.sleep(5)

# 2. Selects radio buttons and checkboxes
driver.find_element(By.ID, "my-check-1").click()                    # UnSelects Checked checkbox
driver.find_element(By.ID, "my-check-1").click()                    # Selects Checked checkbox
driver.find_element(By.ID, "my-check-2").click()                    # Selects Default checkbox
driver.find_element(By.ID, "my-radio-1").click()                    # Selects Checked radio button
driver.find_element(By.ID, "my-radio-2").click()                    # Selects Default radio button
time.sleep(5)

# 3. Chooses an option from a drop-down list using the Select class
dropdown = Select(driver.find_element(By.NAME, "my-select"))        # Locates the dropdown list
dropdown.select_by_visible_text("Two")                              # Selects option "Two" from dropdown
time.sleep(5)

# 4. Submits the form and verifies a confirmation message
driver.find_element(By.TAG_NAME, "button").click()                  # Clicks the Submit button


message = driver.find_element(By.ID, "message").text                # Gets confirmation message text
print("Confirmation Message:", message)                              # Prints confirmation message
time.sleep(5)
driver.quit()
