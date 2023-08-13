from pages.cart_page import Cart
from pages.product_page import ProductPage
from pages.products_page import ProductsPage


def test_open_cart(driver, with_product_in_cart):
    result = with_product_in_cart.get_page_title_text()

    assert result in "Your Cart"


def test_return_to_products_from_cart(driver, logged_in):
    cart = Cart(driver)
    cart.click_on_cart_icon()
    cart.click_on_continue_shopping_button()
    result = cart.get_page_title_text()

    assert result in "Products"


def test_adding_product_to_cart_from_products_page(driver, logged_in):
    products_page = ProductsPage(driver)
    product_title = products_page.get_current_title(0).text
    product_desc = products_page.get_current_desc(0)
    product_price = products_page.get_current_price(0)
    products_page.click_on_add_to_cart_button(0)

    cart = Cart(driver)
    cart.click_on_cart_icon()
    product_title_in_cart = cart.get_current_product_title_in_cart(0).text
    product_desc_in_cart = cart.get_current_desc_in_cart(0)
    product_price_in_cart = cart.get_current_price_in_cart(0)

    assert product_title_in_cart == product_title
    assert product_desc_in_cart == product_desc
    assert product_price_in_cart == product_price


def test_adding_product_to_cart_from_product_page(driver, logged_in):
    product_page = ProductPage(driver)
    product_page.open_product_page(0)
    product_page_title = product_page.get_product_title()
    product_page_desc = product_page.get_product_desc()
    product_page_price = product_page.get_product_price()
    product_page.click_on_add_to_cart_button()

    cart = Cart(driver)
    cart.click_on_cart_icon()
    product_title_in_cart = cart.get_current_product_title_in_cart(0).text
    product_desc_in_cart = cart.get_current_desc_in_cart(0)
    product_price_in_cart = cart.get_current_price_in_cart(0)

    assert product_title_in_cart == product_page_title
    assert product_desc_in_cart == product_page_desc
    assert product_price_in_cart == product_page_price


def test_open_product_from_cart(driver, with_product_in_cart):
    product_title_in_cart = with_product_in_cart.get_current_product_title_in_cart(0).text
    product_desc_in_cart = with_product_in_cart.get_current_desc_in_cart(0)
    product_price_in_cart = with_product_in_cart.get_current_price_in_cart(0)
    with_product_in_cart.click_on_product_title_in_cart(0)

    product_page = ProductPage(driver)
    product_page_title = product_page.get_product_title()
    product_page_desc = product_page.get_product_desc()
    product_page_price = product_page.get_product_price()

    assert product_title_in_cart == product_page_title
    assert product_desc_in_cart == product_page_desc
    assert product_price_in_cart == product_page_price


def test_remove_product_from_cart(driver, with_product_in_cart):
    products = with_product_in_cart.get_all_products_in_cart()
    with_product_in_cart.click_on_remove_button_in_cart(0)
    products_after_click = with_product_in_cart.get_all_products_in_cart()

    assert len(products) > len(products_after_click)
