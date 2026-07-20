"""
Central configuration for the automation suite.
Keeping URLs, credentials and timeouts here avoids magic strings/numbers
scattered across the test and page-object layers.
"""

# ---- Application URLs ----
SAUCEDEMO_URL = "https://www.saucedemo.com"
DEMOQA_BUTTONS_URL = "https://demoqa.com/buttons"
JS_ALERTS_URL = "https://the-internet.herokuapp.com/javascript_alerts"

# ---- Valid credentials ----
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

# ---- Invalid credentials (for negative test) ----
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"

# ---- Product under test ----
TARGET_PRODUCT = "Sauce Labs Backpack"

# ---- Checkout / customer details ----
CUSTOMER_FIRST_NAME = "John"
CUSTOMER_LAST_NAME = "Doe"
CUSTOMER_ZIP = "700156"

# ---- Waits ----
DEFAULT_TIMEOUT = 10  # seconds, used by WebDriverWait across page objects

# ---- Test Case 3 data set: (username, password, expected_result) ----
LOGIN_DATA = [
    ("standard_user", "secret_sauce", "SUCCESS"),
    ("locked_out_user", "secret_sauce", "FAILURE"),
    ("problem_user", "secret_sauce", "SUCCESS"),
    ("standard_user", "wrong_password", "FAILURE"),
]
