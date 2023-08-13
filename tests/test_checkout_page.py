import pytest
from pages.cart_page import Cart
from pages.checkout_page import Checkout


def test_open_checkout_page(driver, open_checkout_page_with_product):
    checkout = Checkout(driver)
    result = checkout.get_page_title_text()

    assert result in "Checkout: Your Information"


def test_cancel_button(driver, open_checkout_page_with_product):
    checkout = Checkout(driver)
    cart = Cart(driver)
    checkout.click_on_cancel_button()
    result = cart.get_page_title_text()

    assert result in "Your Cart"


def test_continue_checkout_with_empty_fields(driver, open_checkout_page_with_product):
    checkout = Checkout(driver)
    checkout.click_on_continue_button()
    result = checkout.find_error_msg()

    assert result.is_displayed()


def test_close_error_msg(driver, open_checkout_page_with_product):
    checkout = Checkout(driver)
    checkout.click_on_continue_button()
    checkout.click_on_close_error_message_button()

    assert not checkout.is_error_message_present()


@pytest.mark.parametrize("firstname, lastname, postalcode", [("name", "", ""),
                                                           ("", "lastname", ""),
                                                           ("", "", "postalcode"),
                                                           ("firstname", "lastname", "")])
def test_continue_checkout_with_invalid_credentials(driver, open_checkout_page_with_product, firstname, lastname, postalcode):
    checkout = Checkout(driver)
    checkout.enter_first_name(firstname)
    checkout.enter_last_name(lastname)
    checkout.enter_postal_code(postalcode)
    checkout.click_on_continue_button()

    assert checkout.is_error_message_present()
