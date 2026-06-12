from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
#Q1
driver.get("https://demoqa.com/text-box")
time.sleep(5)
#Q2
full_name = driver.find_element(By.ID, "userName")
full_name.send_keys("Anurag Singh")

#Q3
email= driver.find_element(By.CSS_SELECTOR, "#userEmail")
email.send_keys("anurag.singh.ece27@heritageit.edu.in")
#Q4
current_address_field = driver.find_element(
    By.XPATH, "//textarea[@id='currentAddress']")
current_address_field.send_keys("CHOWBAGA, ANANDAPUR, KOLKATA-700107")
time.sleep(3)
#Q5
current_address_field.clear()
current_address_field.send_keys("LAKE GARDEN, WEST BENGAL")
time.sleep(3)
#Q6
submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
time.sleep(1)
submit_btn.click()
time.sleep(2)
#Q7
displayed_name = driver.find_element(By.ID, "name").text
print("Displayed Name:", displayed_name)
#Q8
placeholder_text = full_name.get_attribute("placeholder")
print("Placeholder of Full Name:", placeholder_text)
#Q9
all_inputs = driver.find_elements(By.TAG_NAME, "input")
print("Total Input Fields:", len(all_inputs))
#Q10
driver.save_screenshot("submission_result.png")
print("Screenshot saved as submission_result.png")

print("Tag name of Email textbox:", email.tag_name)

driver.quit()