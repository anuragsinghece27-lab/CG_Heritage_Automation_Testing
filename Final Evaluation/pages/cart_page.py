from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_item_names(self):
        return [el.text for el in self.find_all(self.CART_ITEM_NAME)]

    def is_product_in_cart(self, product_name: str) -> bool:
        return product_name in self.get_cart_item_names()

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return self
