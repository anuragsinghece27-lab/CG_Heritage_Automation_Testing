import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import (
    VALID_USERNAME,
    VALID_PASSWORD,
    TARGET_PRODUCT,
    CUSTOMER_FIRST_NAME,
    CUSTOMER_LAST_NAME,
    CUSTOMER_ZIP,
)


@pytest.mark.tc2
def test_end_to_end_purchase_journey(driver):
    # Step 1: Login
    login_page = LoginPage(driver).load()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    products_page = ProductsPage(driver)
    assert products_page.is_products_page_displayed(), "Login failed - Products page not displayed"

    # Step 2: Sort products ascending by price and verify the ordering
    products_page.sort_by_price_low_to_high()
    displayed_prices = products_page.get_displayed_prices()
    assert displayed_prices == sorted(displayed_prices), (
        f"Products are not sorted in ascending price order: {displayed_prices}"
    )

    # Step 3 & 4: Select Sauce Labs Backpack and add it to the cart
    products_page.add_product_to_cart(TARGET_PRODUCT)
    assert products_page.get_cart_item_count() == 1, "Cart badge did not update after adding product"

    # Step 5: Verify the cart contains the selected product
    products_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.is_product_in_cart(TARGET_PRODUCT), f"'{TARGET_PRODUCT}' not found in cart"

    # Step 6: Proceed to checkout
    cart_page.checkout()

    # Step 7: Enter customer details
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_customer_details(CUSTOMER_FIRST_NAME, CUSTOMER_LAST_NAME, CUSTOMER_ZIP)

    # Step 8: Complete the purchase
    checkout_page.finish_purchase()

    # Step 9: Verify order confirmation
    assert checkout_page.is_order_confirmed(), "Order confirmation message was not displayed"
    confirmation = checkout_page.get_confirmation_message()
    assert confirmation == "Thank you for your order!", f"Unexpected confirmation text: '{confirmation}'"
