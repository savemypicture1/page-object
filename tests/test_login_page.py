import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    products = ProductsPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    result = products.get_page_title_text()

    assert result in "Products"


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("standard_user_test", "secret_sauce_test", "invalid_credentials"),
        ("locked_out_user", "secret_sauce", "locked_user"),
        ("", "", "without_credentials"),
    ],
)
def test_login_with_invalid_credentials(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    error_msg = login_page.find_error_msg().text

    assert login_page.ERROR_MSGS[expected_result] in error_msg, "Error message is not displayed"
