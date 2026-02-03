# Question 1 – Selenium WebDriver Basics

# Write a Selenium WebDriver script that:

# 1. Opens a Chrome or Firefox browser

# 2. Navigates to https://example.com

# 3. Prints the page title and URL

# 4. Closes the browser



from selenium import webdriver
import time

def test_open_orangehrm_chrome():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)

    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

    driver.quit()
