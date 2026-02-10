# Question 10 – Selenium Grid Execution

# Write a Selenium script that:
# 1. Connects to Selenium Grid using RemoteWebDriver
# 2. Runs the same test on multiple browsers
# 3. Navigates to a website and verifies the page title
# 4. Prints browser name and platform for each execution





import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# 1. Connects to Selenium Grid using RemoteWebDriver
GRID_URL = "http://localhost:4444/wd/hub"

URL = "https://www.google.com"
EXPECTED_TITLE = "Google"

# 2. Runs the same test on multiple browsers
@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_selenium_grid_execution(browser):

    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        raise ValueError("Unsupported browser")

    options.set_capability("platformName", "WINDOWS")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    try:
        # 3. Navigates to a website and verifies the page title
        driver.get(URL)
        assert EXPECTED_TITLE in driver.title

        # 4. Prints browser name and platform for each execution
        browser_name = driver.capabilities.get("browserName")
        platform_name = driver.capabilities.get("platformName")

        print("Browser:", browser_name)
        print("Platform:", platform_name)

    finally:
        driver.quit()
