from selenium import webdriver  # imports webdriver to control browser
from selenium.webdriver.common.by import By  # imports locator strategy
from selenium.webdriver.common.action_chains import ActionChains  # imports ActionChains for mouse hover
from selenium.webdriver.support.ui import Select, WebDriverWait  # imports Select and WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # imports expected conditions

driver = webdriver.Edge()  # launches Microsoft Edge browser
driver.maximize_window()  # maximizes browser window
driver.get("https://tutorialsninja.com/demo/")  # opens the application URL

wait = WebDriverWait(driver, 10)  # creates explicit wait

assert "Your Store" in driver.title  # verifies title of the page

desktops = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))  # waits for Desktops menu
actions = ActionChains(driver)  # creates ActionChains object
actions.move_to_element(desktops).perform()  # hovers mouse over Desktops menu

mac = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mac")))  # waits for Mac option
mac.click()  # clicks on Mac option

mac_heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))  # locates Mac page heading
assert mac_heading.text == "Mac"  # verifies Mac heading text

sort_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "input-sort"))))  # locates Sort By dropdown
sort_dropdown.select_by_visible_text("Name (A - Z)")  # selects Name (A-Z) option

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick=\"cart.add('41', '1');\"]"))).click()  # clicks Add to Cart button

search_box = wait.until(EC.presence_of_element_located((By.NAME, "search")))  # locates Search text box
search_box.send_keys("Monitors")  # enters Monitors in search box
driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()  # clicks Search button

wait.until(EC.presence_of_element_located((By.ID, "input-search")))  # waits for search page to load

search_criteria = driver.find_element(By.ID, "input-search")  # locates Search Criteria text box
search_criteria.clear()  # clears text from Search Criteria box

driver.find_element(By.NAME, "description").click()  # clicks Search in product descriptions checkbox
driver.find_element(By.ID, "button-search").click()  # clicks Search button again

driver.quit()  # closes the browser
