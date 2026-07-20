import pytest
from pages.buttons_page import ButtonsPage
from pages.js_alerts_page import JsAlertsPage


@pytest.mark.tc4
def test_double_click_button(driver):
    buttons_page = ButtonsPage(driver).load()
    message = buttons_page.perform_double_click()
    assert message == "You have done a double click", f"Unexpected message: '{message}'"


@pytest.mark.tc4
def test_right_click_button(driver):
    buttons_page = ButtonsPage(driver).load()
    message = buttons_page.perform_right_click()
    assert message == "You have done a right click", f"Unexpected message: '{message}'"


@pytest.mark.tc4
def test_js_alert(driver):
    alerts_page = JsAlertsPage(driver).load()
    result = alerts_page.handle_js_alert()
    assert result == "You successfully clicked an alert", f"Unexpected result: '{result}'"


@pytest.mark.tc4
def test_js_confirm_accept(driver):
    alerts_page = JsAlertsPage(driver).load()
    result = alerts_page.handle_js_confirm(accept=True)
    assert result == "You clicked: Ok", f"Unexpected result: '{result}'"


@pytest.mark.tc4
def test_js_confirm_dismiss(driver):
    alerts_page = JsAlertsPage(driver).load()
    result = alerts_page.handle_js_confirm(accept=False)
    assert result == "You clicked: Cancel", f"Unexpected result: '{result}'"


@pytest.mark.tc4
def test_js_prompt_accept(driver):
    alerts_page = JsAlertsPage(driver).load()
    result = alerts_page.handle_js_prompt("Automation Test Input", accept=True)
    assert result == "You entered: Automation Test Input", f"Unexpected result: '{result}'"


@pytest.mark.tc4
def test_js_prompt_dismiss(driver):
    alerts_page = JsAlertsPage(driver).load()
    result = alerts_page.handle_js_prompt("Ignored Input", accept=False)
    assert result == "You entered: null", f"Unexpected result: '{result}'"
