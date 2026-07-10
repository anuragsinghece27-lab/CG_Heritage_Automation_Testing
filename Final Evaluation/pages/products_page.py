from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_products_page_displayed(self) -> bool:
        return self.is_visible(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == "Products"

    def sort_by_price_low_to_high(self):
        from selenium.webdriver.support.ui import Select
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_value("lohi")
        return self

    def get_displayed_prices(self):
        price_elements = self.find_all(self.INVENTORY_ITEM_PRICE)
        return [float(el.text.replace("$", "")) for el in price_elements]

    def add_product_to_cart(self, product_name: str):
        add_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
            f"//button[contains(@id,'add-to-cart')]",
        )
        self.click(add_button)
        return self

    def get_cart_item_count(self) -> int:
        if self.is_visible(self.CART_BADGE, timeout=3):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)
        return self

    def logout(self):
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)
        return self
