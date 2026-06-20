from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Case1
driver = webdriver.Chrome()
driver.maximize_window()

#Case2
driver.get("https://practicetestautomation.com/practice-test-login/")

assert "Test Login" in driver.title
print("Login Page Loaded Successfully")

#Case3
username = driver.find_element(By.ID, "username")
username.send_keys("student")

#Case4
password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

#Case5
login_button = driver.find_element(By.ID, "submit")
login_button.click()
time.sleep(2)

#Case6
msg= driver.find_element(By.TAG_NAME,"h1").text

assert "Logged In Successfully" in msg
print("Login Verification Passed")

#Case7
current_url = driver.current_url
print("Current URL:", current_url)

assert "logged-in-successfully" in current_url
print("URL Verification Passed")

#Case8
print("Message:", msg)


#Case9
driver.save_screenshot("login_success.png")
print("Screenshot Saved")

#Case10
logout_btn = driver.find_element(By.LINK_TEXT, "Log out")
logout_btn.click()
time.sleep(2)

assert "practice-test-login" in driver.current_url
print("Logout Successful")
print("Redirected Back To Login Page")

#Case11
driver.quit()


