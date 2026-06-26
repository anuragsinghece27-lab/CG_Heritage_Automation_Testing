import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    # Login Page Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    # Logout Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    # Login Method
    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    # Logout Method
    def logout(self):
        print("Clicking Menu Button...")
        self.click(self.MENU_BUTTON)

        # Wait for the side menu to open
        self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        )

        time.sleep(2)

        print("Clicking Logout Button...")
        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        ).click()

        time.sleep(2)

        print("Logout Completed")