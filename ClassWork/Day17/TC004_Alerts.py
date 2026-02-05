from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://letcode.in/alert")

wait = WebDriverWait(driver, 10)

# Accept Alert
driver.find_element(By.ID, "accept").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# driver.quit()


# Confirm Alert
driver.find_element(By.ID, "confirm").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# Prompt Alert
driver.find_element(By.ID, "prompt").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Prashant Kumar Jha")
alert.accept()

# Modern Alert

driver.find_element(By.ID, "modern").click()

try:
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except NoAlertPresentException:
    print("Alert not present : Modern alert clicked (HTML-based, no browser alert).")


driver.quit()
