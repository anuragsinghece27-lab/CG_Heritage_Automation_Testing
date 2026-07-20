from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import JS_ALERTS_URL, DEFAULT_TIMEOUT


class JsAlertsPage(BasePage):
    JS_ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT_TEXT = (By.ID, "result")

    def load(self):
        self.driver.get(JS_ALERTS_URL)
        return self

    def handle_js_alert(self) -> str:
        self.click(self.JS_ALERT_BTN)
        alert = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.alert_is_present())
        alert.accept()
        return self.get_text(self.RESULT_TEXT)

    def handle_js_confirm(self, accept: bool = True) -> str:
        self.click(self.JS_CONFIRM_BTN)
        alert = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.alert_is_present())
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return self.get_text(self.RESULT_TEXT)

    def handle_js_prompt(self, input_text: str, accept: bool = True) -> str:
        self.click(self.JS_PROMPT_BTN)
        alert = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.alert_is_present())
        if accept:
            alert.send_keys(input_text)
            alert.accept()
        else:
            alert.dismiss()
        return self.get_text(self.RESULT_TEXT)
