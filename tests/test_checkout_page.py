from pages.cart_page import Cart


def test_open_checkout_page(driver, logged_in):
    pass


def test_cancel_button(driver, logged_in):
    pass


def test_continue_checkout_with_empty_fields(driver, logged_in):
    pass


def test_continue_checkout_with_filled_first_name(driver, logged_in):
    pass


def test_continue_checkout_with_filled_first_and_last_name(driver, logged_in):
    pass


def test_continue_checkout_with_only_spaces_in_fields(driver, logged_in):
    pass


def test_checkout_with_product(driver, logged_in, with_product_in_cart):
    pass


def test_checkout_without_product(driver, logged_in):
    cart = Cart(driver)
    cart.click_on_cart_icon()
    cart.click_on_checkout_button()
