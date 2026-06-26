from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_inventory_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)