from selenium import webdriver  # imports webdriver to control browser
from selenium.webdriver.common.by import By  # imports locator strategy
from selenium.webdriver.common.action_chains import ActionChains  # imports ActionChains for mouse hover
from selenium.webdriver.support.ui import Select, WebDriverWait  # imports Select and WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # imports expected conditions

driver = webdriver.Edge()  # launches Microsoft Edge browser
driver.maximize_window()  # maximizes browser window
driver.get("https://tutorialsninja.com/demo/")  # opens the application URL

wait = WebDriverWait(driver, 10)  # creates explicit wait

desktops = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))  # waits for Desktops menu
actions = ActionChains(driver)  # creates ActionChains object
actions.move_to_element(desktops).perform()  # hovers mouse over Desktops menu

mac = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mac")))  # waits for Mac option
mac.click()  # clicks on Mac option

sort_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "input-sort"))))  # locates Sort By dropdown
sort_dropdown.select_by_visible_text("Name (A - Z)")  # selects Name (A-Z)

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick=\"cart.add('41', '1');\"]"))).click()  # clicks Add to Cart

driver.quit()  # closes the browser
