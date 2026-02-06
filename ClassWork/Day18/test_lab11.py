from selenium import webdriver  # imports webdriver to control browser
from selenium.webdriver.common.by import By  # imports locator strategy
from selenium.webdriver.common.action_chains import ActionChains  # imports ActionChains for mouse hover
from selenium.webdriver.support.ui import Select, WebDriverWait  # imports Select and WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # imports expected conditions


class HomePage:
    def __init__(self, driver):
        self.driver = driver  # stores driver reference
        self.wait = WebDriverWait(driver, 10)  # creates explicit wait

        self.desktops = (By.LINK_TEXT, "Desktops")  # locator for Desktops menu
        self.mac = (By.PARTIAL_LINK_TEXT, "Mac")  # locator for Mac option
        self.search_box = (By.NAME, "search")  # locator for search text box
        self.search_button = (By.CSS_SELECTOR, "button.btn-default")  # locator for search button

    def open_mac_page(self):
        desktops_menu = self.wait.until(EC.visibility_of_element_located(self.desktops))  # waits for Desktops menu
        ActionChains(self.driver).move_to_element(desktops_menu).perform()  # hovers on Desktops menu
        self.wait.until(EC.element_to_be_clickable(self.mac)).click()  # clicks Mac option

    def search_product(self, product_name):
        self.wait.until(EC.presence_of_element_located(self.search_box)).send_keys(product_name)  # enters search text
        self.driver.find_element(*self.search_button).click()  # clicks Search button


class MacPage:
    def __init__(self, driver):
        self.driver = driver  # stores driver reference
        self.wait = WebDriverWait(driver, 10)  # creates explicit wait

        self.heading = (By.TAG_NAME, "h2")  # locator for Mac heading
        self.sort_dropdown = (By.ID, "input-sort")  # locator for Sort By dropdown
        self.add_to_cart = (By.XPATH, "//button[@onclick=\"cart.add('41', '1');\"]")  # locator for Add to Cart
        self.search_criteria = (By.ID, "input-search")  # locator for Search Criteria
        self.description_checkbox = (By.NAME, "description")  # locator for description checkbox
        self.search_button = (By.ID, "button-search")  # locator for Search button

    def verify_mac_heading(self):
        assert self.wait.until(EC.visibility_of_element_located(self.heading)).text == "Mac"  # verifies Mac heading

    def sort_by_name_az(self):
        Select(self.wait.until(EC.presence_of_element_located(self.sort_dropdown))).select_by_visible_text("Name (A - Z)")  # sorts Name A-Z

    def add_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()  # clicks Add to Cart

    def advanced_search(self):
        criteria_box = self.wait.until(EC.presence_of_element_located(self.search_criteria))  # locates Search Criteria
        criteria_box.clear()  # clears Search Criteria
        self.driver.find_element(*self.description_checkbox).click()  # selects description checkbox
        self.driver.find_element(*self.search_button).click()  # clicks Search button


driver = webdriver.Edge()  # launches Edge browser
driver.maximize_window()  # maximizes browser window
driver.get("https://tutorialsninja.com/demo/")  # opens application URL

home = HomePage(driver)  # creates HomePage object
mac = MacPage(driver)  # creates MacPage object

home.open_mac_page()  # opens Mac page
mac.verify_mac_heading()  # verifies Mac heading
mac.sort_by_name_az()  # sorts products
mac.add_product_to_cart()  # adds product to cart
home.search_product("Monitors")  # searches Monitors
mac.advanced_search()  # performs advanced search

driver.quit()  # closes the browser
