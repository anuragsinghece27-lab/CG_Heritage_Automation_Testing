from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

# Capture Actual Title
actual_title = driver.title  #OrangeHRM
print("Actual Title:", actual_title)

# Expected Title
expected_title = "OrangeHRM"

# Verify Title
if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")

# Close Browser
driver.quit()