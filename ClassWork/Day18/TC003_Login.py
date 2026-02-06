from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions

import sys
import os
sys.path.append(os.path.abspath(r"D:\PythonProject\Prashant Kumar Jha\ClassWork\Day18"))
from TC004_LoginPage import loginpage

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(5)
loginobj=loginpage(driver)

loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")

loginobj.clicklogin()
time.sleep(10)
