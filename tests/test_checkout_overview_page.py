from pages.cart_page import Cart
from pages.checkout_complete_page import CheckoutComplete
from pages.checkout_overview_page import CheckoutOverview
from pages.checkout_page import Checkout
from pages.product_page import ProductPage
from pages.products_page import ProductsPage


def test_open_checkout_overview_page(driver, open_checkout_overview_page_with_product):
    checkout_overview = CheckoutOverview(driver)
    result = checkout_overview.get_page_title_text()

    assert result in "Checkout: Overview"


def test_cancel_button(driver, open_checkout_overview_page_with_product):
    checkout_overview = CheckoutOverview(driver)
    products = ProductsPage(driver)
    checkout_overview.click_on_cancel_button()
    result = products.get_page_title_text()

    assert result in "Products"


def test_open_product_from_checkout(driver, open_checkout_overview_page_with_product):
    checkout_overview = CheckoutOverview(driver)
    product_title_in_checkout = checkout_overview.get_current_product_title_in_checkout(0).text
    product_desc_in_checkout= checkout_overview.get_current_desc_in_checkout(0)
    product_price_in_checkout = checkout_overview.get_current_price_in_checkout(0)
    checkout_overview.click_on_product_title_in_checkout(0)

    product_page = ProductPage(driver)
    product_page_title = product_page.get_product_title()
    product_page_desc = product_page.get_product_desc()
    product_page_price = product_page.get_product_price()

    assert product_title_in_checkout == product_page_title
    assert product_desc_in_checkout == product_page_desc
    assert product_price_in_checkout == product_page_price


def test_current_product_in_checkout(driver, with_product_in_cart):
    cart = Cart(driver)
    product_title_in_cart = cart.get_current_product_title_in_cart(0).text
    product_desc_in_cart = cart.get_current_desc_in_cart(0)
    product_price_in_cart = cart.get_current_price_in_cart(0)
    cart.click_on_checkout_button()

    checkout = Checkout(driver)
    checkout.enter_first_name("Hello")
    checkout.enter_last_name("World")
    checkout.enter_postal_code("Postal Code")
    checkout.click_on_continue_button()

    checkout_overview = CheckoutOverview(driver)
    product_title_in_checkout = checkout_overview.get_current_product_title_in_checkout(0).text
    product_desc_in_checkout = checkout_overview.get_current_desc_in_checkout(0)
    product_price_in_checkout = checkout_overview.get_current_price_in_checkout(0)
    total_price = checkout_overview.get_sub_total_price()
    result_total_price = checkout_overview.get_sum_of_products()

    assert product_title_in_checkout == product_title_in_cart
    assert product_desc_in_checkout == product_desc_in_cart
    assert product_price_in_checkout == product_price_in_cart
    assert total_price == result_total_price


def test_sum_of_total_price(driver, open_checkout_overview_page_with_same_products):
    checkout_overview = CheckoutOverview(driver)
    total_sum_of_products = checkout_overview.get_sum_of_products()
    counting_tax = checkout_overview.counting_of_tax()

    sub_total_price = checkout_overview.get_sub_total_price()
    tax = checkout_overview.get_tax()
    final_total_price = checkout_overview.get_final_total_price()

    assert total_sum_of_products == sub_total_price
    assert counting_tax == tax
    assert total_sum_of_products + counting_tax == final_total_price


def test_buying_product(driver, open_checkout_overview_page_with_product):
    checkout_overview = CheckoutOverview(driver)
    checkout_complete = CheckoutComplete(driver)
    checkout_overview.click_on_finish_button()
    result = checkout_complete.get_page_title_text()

    assert result in "Checkout: Complete!"
