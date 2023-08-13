from pages.cart_page import Cart
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from pages.sidebar import Sidebar


def test_open_sidebar(driver, with_open_sidebar):
    sidebar = Sidebar(driver)
    result = sidebar.is_sidebar_displayed()

    assert result == "false"


def test_close_sidebar_by_x_button(driver, with_open_sidebar):
    sidebar = Sidebar(driver)
    sidebar.click_on_x_button()
    result = sidebar.is_sidebar_displayed()

    assert result == "true"


def test_close_sidebar_by_escape_key(driver, with_open_sidebar):
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
    result = products.get_page_title_text()

    assert result in "Products"


def test_all_items_from_cart_page(driver, logged_in):
    cart = Cart(driver)
    sidebar = Sidebar(driver)
    products = ProductsPage(driver)
    cart.click_on_cart_icon()
    sidebar.click_on_burger_menu()
    sidebar.click_on_items()
    result = products.get_page_title_text()

    assert result in "Products"


def test_about(driver, with_open_sidebar):
    sidebar = Sidebar(driver)
    sidebar.click_on_about()
    meta_title = sidebar.get_page_meta_title()

    assert meta_title in "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"


def test_logout(driver, with_open_sidebar):
    sidebar = Sidebar(driver)
    login_page = LoginPage(driver)
    sidebar.click_on_logout()

    assert login_page.is_login_button_visible()


def test_saving_products_in_cart_after_logout(driver, with_product_in_cart):
    sidebar = Sidebar(driver)
    sidebar.click_on_burger_menu()
    sidebar.click_on_logout()

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    cart = Cart(driver)
    cart.click_on_cart_icon()
    result = cart.get_all_products_in_cart()

    assert len(result) > 0


def test_reset_app_state_on_products_page(driver, logged_in):
    products_page = ProductsPage(driver)
    products_page.click_on_add_to_cart_button(0)
    text_button = products_page.get_current_card_button(0).text

    sidebar = Sidebar(driver)
    sidebar.click_on_burger_menu()
    sidebar.click_on_reset_app_state()
    text_button_after_reset = products_page.get_current_card_button(0).text

    assert text_button != text_button_after_reset, "Products are not removed from cart"


def test_reset_app_state_on_product_page(driver, logged_in):
    product_page = ProductPage(driver)
    product_page.open_product_page(0)
    product_page.click_on_add_to_cart_button()
    text_button = product_page.get_button_text()

    sidebar = Sidebar(driver)
    sidebar.click_on_burger_menu()
    sidebar.click_on_reset_app_state()
    text_button_after_reset = product_page.get_button_text()

    assert text_button != text_button_after_reset, "Products are not removed from cart"


def test_reset_app_state_on_cart(driver, with_product_in_cart):
    products = with_product_in_cart.get_all_products_in_cart()

    sidebar = Sidebar(driver)
    sidebar.click_on_burger_menu()
    sidebar.click_on_reset_app_state()

    products_after_reset = with_product_in_cart.get_all_products_in_cart()

    assert len(products) != len(products_after_reset), "Products are not removed from cart"
