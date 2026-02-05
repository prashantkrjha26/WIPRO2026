from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://letcode.in/window")
time.sleep(5)
driver.find_element(By.ID,"multi").click()
windows=driver.window_handles
for child in windows:
    driver.switch_to.window(child)
    time.sleep(5)
    print("title",driver.current_url)
