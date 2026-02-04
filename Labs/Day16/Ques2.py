# Question 4 – Browser Navigation

# Write a Selenium WebDriver script that:

# 1. Opens a browser and navigates to https://example.com or https://tutorialsninja.com/demo/

# 2. Navigates to another page on the same site

# 3. Uses back(), forward(), and refresh()

# 4. Prints the page title after each navigation

# 5. Closes the browser



from selenium import webdriver
import time

# Question 4 – Browser Navigation
# Step 1: Open a browser and navigate to https://tutorialsninja.com/demo/
driver = webdriver.Edge()
driver.get("https://tutorialsninja.com/demo/")
print("Title after opening home page:", driver.title)
time.sleep(2)

# Step 2: Navigate to another page on the same site
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
print("Title after navigating to another page:", driver.title)
time.sleep(2)

# Step 3: Use back() method
driver.back()
print("Title after back navigation:", driver.title)
time.sleep(2)

# Step 3: Use forward() method
driver.forward()
print("Title after forward navigation:", driver.title)
time.sleep(2)

# Step 3: Use refresh() method
driver.refresh()
print("Title after refresh:", driver.title)
time.sleep(2)

# Step 5: Close the browser
driver.quit()
