import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart
from pages.checkout_page import Checkout
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.sidebar import Sidebar


#  Launch tests without opening browser
# @pytest.fixture
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.saucedemo.com/")
#     yield driver
#     driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()


@pytest.fixture
def with_open_sidebar(driver, logged_in):
    sidebar = Sidebar(driver)
    sidebar.click_on_burger_menu()


@pytest.fixture
def with_product_in_cart(driver, logged_in):
    products_page = ProductsPage(driver)
    cart = Cart(driver)
    products_page.click_on_add_to_cart_button(0)
    cart.click_on_cart_icon()
    return cart


@pytest.fixture
def open_checkout_overview_page_with_product(driver, with_product_in_cart):
    cart = Cart(driver)
    checkout = Checkout(driver)
    cart.click_on_checkout_button()
    checkout.enter_first_name("test")
    checkout.enter_last_name("test")
    checkout.enter_postal_code("test")
    checkout.click_on_continue_button()


@pytest.fixture
def open_checkout_page_with_product(driver, with_product_in_cart):
    cart = Cart(driver)
    cart.click_on_checkout_button()


@pytest.fixture
def open_checkout_overview_page_with_same_products(driver, logged_in):
    products_page = ProductsPage(driver)
    for num in range(0, 4):
        products_page.click_on_add_to_cart_button(num)
    cart = Cart(driver)
    cart.click_on_cart_icon()
    cart.click_on_checkout_button()
    checkout = Checkout(driver)
    checkout.enter_first_name("test")
    checkout.enter_last_name("test")
    checkout.enter_postal_code("test")
    checkout.click_on_continue_button()
