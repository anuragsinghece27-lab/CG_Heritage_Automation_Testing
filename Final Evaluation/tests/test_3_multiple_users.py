import os
import csv
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import LOGIN_DATA

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
RESULTS_FILE = os.path.join(RESULTS_DIR, "login_results.csv")


def _record_result(username, password, expected, observed):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    file_exists = os.path.isfile(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Username", "Password", "Expected Result", "Observed Result", "Match"])
        writer.writerow([username, password, expected, observed, expected == observed])


@pytest.mark.tc3
@pytest.mark.parametrize("username,password,expected_result", LOGIN_DATA)
def test_login_multiple_users(driver, username, password, expected_result):
    login_page = LoginPage(driver).load()
    login_page.login(username, password)

    products_page = ProductsPage(driver)

    if products_page.is_products_page_displayed():
        observed_result = "SUCCESS"
    elif login_page.is_error_displayed():
        observed_result = "FAILURE"
    else:
        observed_result = "UNKNOWN"

    _record_result(username, password, expected_result, observed_result)

    assert observed_result == expected_result, (
        f"Login result mismatch for user '{username}': "
        f"expected '{expected_result}', observed '{observed_result}'"
    )
