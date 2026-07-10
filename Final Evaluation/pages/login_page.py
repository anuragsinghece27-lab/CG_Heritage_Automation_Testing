from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import SAUCEDEMO_URL


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    def load(self):
        self.driver.get(SAUCEDEMO_URL)
        return self

    def is_login_page_displayed(self) -> bool:
        return (
            self.is_visible(self.LOGIN_LOGO)
            and self.is_visible(self.USERNAME_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
        )

    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE, timeout=5)
