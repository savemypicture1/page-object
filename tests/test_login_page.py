import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_login_with_valid_date(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    time.sleep(3)



def test_with_ivalid_data():
    pass

def test_with_locked_out_user():
    pass

def test_login_without_credentials(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()

    error_msg = driver.find_element(By.CSS_SELECTOR, "h3")

    assert error_msg.is_displayed(), "Error message is not displayed"

