import pytest
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.regression
def test_login():

    # Launch Browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Open Website
    driver.get("https://www.saucedemo.com/")

    # Read credentials from CSV
    data = pd.read_csv("data/login.csv")

    username = data["username"][0]
    password = data["password"][0]

    # Create Page Objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Login using CSV data
    login.login(username, password)

    # Assertion 1: Login Successful
    assert "inventory.html" in driver.current_url

    # Assertion 2: Inventory Page Title
    assert inventory.get_inventory_title() == "Products"

    # Assertion 3: URL Verification
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Add Product to Cart
    inventory.add_product_to_cart()

    # Assertion 4: Cart Badge Count = 1
    assert inventory.get_cart_badge_count() == "1"

    # Logout
    login.logout()

    # Wait until redirected to Login Page
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/")
    )

    # Assertion 5: Logout Successful
    assert driver.current_url == "https://www.saucedemo.com/"

    # Close Browser
    driver.quit()