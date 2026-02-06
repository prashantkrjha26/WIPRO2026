# Question 8 – Handling iFrames and Windows

# Write a Selenium script that:
# 1. Switches to an iframe and enters text in an input field inside it
# 2. Switches back to the main content
# 3. Opens a new browser window or tab
# 4. Switches between windows and prints each window title
# 5. Closes the child window and returns to the parent




from selenium import webdriver                      # Import Edge browser control
from selenium.webdriver.common.by import By         # Import locator strategies
from selenium.webdriver.support.ui import WebDriverWait  # Import explicit wait
from selenium.webdriver.support import expected_conditions as EC  # Import wait conditions
import time                                         # Import time for delay

# Part 2: Store URLs used in the test
IFRAME_URL = "https://the-internet.herokuapp.com/iframe"  # Part 1: Page containing iframe
ORANGEHRM_URL = "https://opensource-demo.orangehrmlive.com/"  # Part 3: Page for window handling

driver = webdriver.Edge()                           # Launch Edge browser
driver.maximize_window()                            # Maximize browser window
wait = WebDriverWait(driver, 10)                    # Define wait time

# Part 1: Switch to an iframe and enter text inside it
driver.get(IFRAME_URL)                              # Part 1: Open iframe page
driver.switch_to.frame("mce_0_ifr")                 # Part 1: Switch into iframe

text_area = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))  # Part 1: Locate text area

driver.execute_script("arguments[0].innerHTML = '';", text_area)  # Part 1: Clear iframe text
time.sleep(3)
driver.execute_script("arguments[0].innerHTML = 'Handling iframe using Selenium';",
                      text_area)                          # Part 1: Enter text inside iframe
time.sleep(5)

# Part 2: Switch back to the main content
driver.switch_to.default_content()                  # Part 2: Return to main page
time.sleep(5)

# Part 3: Open a new browser window or tab
driver.get(ORANGEHRM_URL)                           # Part 3: Open OrangeHRM page
parent_window = driver.current_window_handle        # Part 3: Store parent window id
time.sleep(5)

driver.execute_script("window.open('https://www.amazon.com/','_blank');")     # Part 3: Open new browser tab

time.sleep(5)                                       # Part 3: Wait for new tab to open

# Part 4: Switch between windows and print each window title
all_windows = driver.window_handles                 # Part 4: Get all window ids

for window in all_windows:
    driver.switch_to.window(window)                 # Part 4: Switch to window
    print("Window Title:", driver.title)            # Part 4: Print window title

time.sleep(5)

# Part 5: Close the child window and return to the parent
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)             # Part 5: Switch to child window
        driver.close()                              # Part 5: Close child window

driver.switch_to.window(parent_window)              # Part 5: Switch back to parent window
print("Parent Window Title:", driver.title)         # Part 5: Print parent window title


time.sleep(5)
driver.quit()                                       # Part 5: Close browser

