from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from utils.config import DEMOQA_BUTTONS_URL


class ButtonsPage(BasePage):
    DOUBLE_CLICK_BTN = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BTN = (By.ID, "rightClickBtn")
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")

    def load(self):
        self.driver.get(DEMOQA_BUTTONS_URL)
        return self

    def _dismiss_overlays(self):

        self.driver.execute_script(
            "document.querySelectorAll('#fixedban, .adsbygoogle, footer').forEach(el => el.remove());"
        )

    def perform_double_click(self) -> str:
        self._dismiss_overlays()
        button = self.find_clickable(self.DOUBLE_CLICK_BTN)
        ActionChains(self.driver).double_click(button).perform()
        return self.get_text(self.DOUBLE_CLICK_MESSAGE)

    def perform_right_click(self) -> str:
        self._dismiss_overlays()
        button = self.find_clickable(self.RIGHT_CLICK_BTN)
        ActionChains(self.driver).context_click(button).perform()
        return self.get_text(self.RIGHT_CLICK_MESSAGE)
