# Question 3 – Locators & Object Identification

# 1. Finds elements using ID, Name, Class Name, XPath, and CSS Selector

# 2. Enters text in input fields and clicks a submit button

# 3. Validates a message displayed on the page



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class TestLocatorsAndObjectIdentification:

    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def teardown_method(self):
        time.sleep(2)
        self.driver.quit()

    def test_question_3(self):
        # Open TutorialsNinja Register page
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

        # Question Part 1
        # Find elements using ID, Name, Class Name, XPath, and CSS Selector

        # Using ID
        first_name = self.driver.find_element(By.ID, "input-firstname")

        # Using Name
        last_name = self.driver.find_element(By.NAME, "lastname")

        # Using Class Name
        continue_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")

        # Using XPath
        email_field = self.driver.find_element(By.XPATH, "//input[@id='input-email']")

        # Using CSS Selector
        telephone_field = self.driver.find_element(By.CSS_SELECTOR, "input#input-telephone")

        # Question Part 2
        # Enter text in input fields and click submit button

        first_name.send_keys("Prashant Kumar")
        last_name.send_keys("Jha")
        unique_number = random.randint(1000, 9999)
        unique_email = f"prashantkumarjha{unique_number}@test.com"
        email_field.send_keys(unique_email)
        telephone_field.send_keys("9876543210")

        self.driver.find_element(By.ID, "input-password").send_keys("Test@123")
        self.driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

        self.driver.find_element(By.NAME, "agree").click()
        continue_button.click()

        # Question Part 3
        # Validate a message displayed on the page

        success_message = self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        assert "Your Account Has Been Created!" in success_message
