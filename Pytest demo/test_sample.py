from selenium import webdriver
def test_google_title():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com/")
    assert "Google" == driver.title
    driver.quit()
