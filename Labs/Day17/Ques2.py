# Question 6 – Handling Alerts and Pop-ups

# Write a Selenium script that:
# 1. Triggers a JavaScript alert
# 2. Accepts the alert and prints its message
# 3. Dismisses a confirmation pop-up
# 4. Enters text in a prompt alert and accepts it
# 5. Verifies the result displayed on the page



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://letcode.in/alert")

wait = WebDriverWait(driver, 10)

# 1. Triggers a JavaScript alert
driver.find_element(By.ID, "accept").click()

# 2. Accepts the alert and prints its message
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Alert message:", alert.text)
alert.accept()

# 3. Dismisses a confirmation pop-up
driver.find_element(By.ID, "confirm").click()
wait.until(EC.alert_is_present())
confirm_alert = driver.switch_to.alert
print("Confirmation message:", confirm_alert.text)
confirm_alert.dismiss()

# 4. Enters text in a prompt alert and accepts it
driver.find_element(By.ID, "prompt").click()
wait.until(EC.alert_is_present())
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Selenium Alert Test Performed Successfully by Prashant Kumar Jha")
prompt_alert.accept()

# 5. Verifies the result displayed on the page
result_text = driver.find_element(By.ID, "myName").text
print("Result on page:", result_text)

time.sleep(5)
driver.quit()
