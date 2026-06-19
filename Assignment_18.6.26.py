from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
#module1
#1,2
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
#3
driver.find_element(By.ID, "username").send_keys("tomsmith")
#4
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
#5
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#6
msg = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in msg
print('Login Status:', msg)
#7
driver.save_screenshot('full_page.png')
print('Screenshot saved as full_page.png')

#module2
dropdown = Select(driver.find_element(By.ID, "dropdown"))
#1
dropdown.select_by_index(1)
time.sleep(2)
#2
dropdown.select_by_value("2")
time.sleep(2)
#3
dropdown.select_by_visible_text("Option 1")
time.sleep(2)

#module3
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
if not checkbox[0].is_selected():
    checkbox[0].click()

print(checkbox[0].is_selected())
time.sleep(2)

#module4
#1,2,3
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

#module5
parent = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()

all_windows = driver.window_handles

for window in all_windows:

    if window != parent:
        driver.switch_to.window(window)

        print(driver.title)

        driver.close()

driver.switch_to.window(parent)

#module6
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

box = driver.find_element(By.ID, "tinymce")
box.clear()
box.send_keys("Hello Selenium")

driver.switch_to.default_content()

time.sleep(3)

#module7
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")

text = driver.find_element(By.TAG_NAME, "body").text
print(text)

driver.switch_to.default_content()


#module8
driver.find_element(By.XPATH, "//button[text()='Enable']").click()

# Wait until the text box becomes enabled
textbox = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.XPATH, "//form[@id='input-example']/input")
)

WebDriverWait(driver, 10).until(
    lambda d: textbox.is_enabled()
)

print("Textbox is now enabled.")

#module9
#for rows
rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")

for row in rows:
    print(row.text)
#for columns
columns = driver.find_elements(By.XPATH,"//table[@id='table1']/thead/tr/th")

for column in columns:
    print(column.text)

#module10
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

ActionChains(driver).drag_and_drop(source, target).perform()


#module11
actions = ActionChains(driver)
actions.context_click(box).perform()

#module12
element = driver.find_element(By.ID, "sibling-50.1")
# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView();",element)

# Highlight the element
driver.execute_script("arguments[0].style.border='3px solid red';",element)

print("Element scrolled into view and highlighted.")



