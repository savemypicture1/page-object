import time
from pages.login_page import LoginPage


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    time.sleep(3)


def test_with_ivalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user_test")
    login_page.enter_password("secret_sauce_test")
    login_page.click_login_button()

    error_msg = login_page.find_error_msg().text

    assert login_page.ERROR_MSGS["invalid_credentials"] in error_msg, "Error message is not displayed"


def test_with_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    error_msg = login_page.find_error_msg().text

    assert login_page.ERROR_MSGS["locked_user"] in error_msg, "Error message is not displayed"


def test_login_without_credentials(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()

    error_msg = login_page.find_error_msg().text

    assert login_page.ERROR_MSGS["without_credentials"] in error_msg, "Error message is not displayed"
