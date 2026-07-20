"""
Factory responsible for creating and configuring the Selenium WebDriver
instance. Centralising this means every test gets an identically
configured browser, and switching browser/headless mode is a one-line
change instead of a find-and-replace across the whole suite.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless: bool = False):
    """
    Builds and returns a configured Chrome WebDriver instance.

    :param headless: run Chrome without a visible UI (useful for CI).
    """
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    # Reduces noisy "USB device" / DevTools console log spam on Windows CI agents
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(2)
    return driver
