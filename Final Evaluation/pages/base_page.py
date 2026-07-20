from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)
