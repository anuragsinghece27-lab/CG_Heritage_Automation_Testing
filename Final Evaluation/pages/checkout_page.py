from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    def enter_customer_details(self, first_name: str, last_name: str, zip_code: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ZIP_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_purchase(self):
        self.click(self.FINISH_BUTTON)
        return self

    def get_confirmation_message(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def is_order_confirmed(self) -> bool:
        return self.is_visible(self.COMPLETE_HEADER) and "Thank you" in self.get_confirmation_message()
