import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD


@pytest.mark.tc1
def test_valid_login_and_logout(driver):
    login_page = LoginPage(driver).load()

    # Step 1 & 2: application launched, login page displayed
    assert login_page.is_login_page_displayed(), "Login page was not displayed on launch"

    # Step 3: login with valid credentials
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # Step 4: verify user reaches Products page
    products_page = ProductsPage(driver)
    assert products_page.is_products_page_displayed(), "User did not land on the Products page after valid login"

    # Step 5: logout
    products_page.logout()
    assert login_page.is_login_page_displayed(), "User was not returned to the Login page after logout"


@pytest.mark.tc1
def test_invalid_login_shows_error(driver):
    login_page = LoginPage(driver).load()
    assert login_page.is_login_page_displayed(), "Login page was not displayed on launch"

    # Step 6: attempt login with invalid credentials
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    # Step 7: verify error message
    assert login_page.is_error_displayed(), "No error message was displayed for invalid credentials"
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text or "do not match" in error_text, (
        f"Unexpected error message text: '{error_text}'"
    )
