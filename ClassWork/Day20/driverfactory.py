from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRIDURL = "http://10.198.36.51:4444/wd/hub"


def getdriver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")

    elif browser == "firefox":
        options = FirefoxOptions()

    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRIDURL,
        options=options
    )

    driver.maximize_window()
    return driver
