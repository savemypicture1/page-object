from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from pages.sidebar import Sidebar


def test_open_sidebar(driver, logged_in, with_open_sidebar):
    sidebar = Sidebar(driver)
    result = sidebar.is_sidebar_displayed()

    assert result == "false"


def test_close_sidebar_by_x_button(driver, logged_in, with_open_sidebar):
    sidebar = Sidebar(driver)
    sidebar.click_on_x_button()
    result = sidebar.is_sidebar_displayed()

    assert result == "true"


def test_close_sidebar_by_escape_key(driver, logged_in, with_open_sidebar):
    sidebar = Sidebar(driver)
    sidebar.close_sidebar_by_esc()
    result = sidebar.is_sidebar_displayed()

    assert result == "true"


def test_all_items_from_product_page(driver, logged_in):
    product_page = ProductPage(driver)
    sidebar = Sidebar(driver)
    products = ProductsPage(driver)
    product_page.open_product_page(0)
    sidebar.click_on_burger_menu()
    sidebar.click_on_items()
    result = products.get_page_title()

    assert result.is_displayed()

def test_all_items_from_cart_page(driver, logged_in):
    pass

def test_about(driver, logged_in, with_open_sidebar):
    sidebar = Sidebar(driver)
    sidebar.click_on_about()
    title = sidebar.get_page_title()

    assert "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing" in title


def test_logout(driver, logged_in, with_open_sidebar):
    sidebar = Sidebar(driver)
    login_page = LoginPage(driver)
    sidebar.click_on_logout()

    assert login_page.is_login_button_visible()


def test_reset_app_state(driver, logged_in):
    pass
