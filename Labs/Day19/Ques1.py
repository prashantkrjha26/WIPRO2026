# Question 9 – Selenium Waits

# Write a Selenium script that:
# 1. Demonstrates implicit wait
# 2. Demonstrates explicit wait for an element to become clickable
# 3. Demonstrates fluent wait with a polling interval
# 4. Prints a message when the element is available for interaction




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize browser
driver.maximize_window()

# Part 1: Implicit wait
driver.implicitly_wait(10)

# Part 2: Explicit wait for element to be clickable
explicit_wait = WebDriverWait(driver, 15)
login_button = explicit_wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
print("Element is clickable using explicit wait")

# Part 3: Fluent wait with polling interval
fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

username_field = fluent_wait.until(
    lambda driver: driver.find_element(By.NAME, "username")
)
print("Element found using fluent wait")

# Part 4: Print message when element is available for interaction
if username_field.is_enabled():
    print("Element is available for interaction")

time.sleep(3)
driver.quit()
