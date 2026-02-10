import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os
sys.path.append(os.path.abspath(r"D:\PythonProject\Prashant Kumar Jha\ClassWork\Day20"))
from driverfactory import getdriver

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_title(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_search(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com/")
    searchbox = driver.find_element("name", "q")
    searchbox.send_keys("Selenium Grid")
    searchbox.submit()
    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium Grid - Google Search")
    )

    assert "Selenium Grid - Google Search" in driver.title
    driver.quit()
