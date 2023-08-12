from pages.product_page import ProductPage
from pages.products_page import ProductsPage


def test_back_to_products_button(driver, logged_in):
    product_page = ProductPage(driver)
    products = ProductsPage(driver)
    product_page.open_product_page(0)
    product_page.click_on_back_products_button()

    result = products.get_page_title()

    assert result.is_displayed()


def test_product_button(driver, logged_in):
    product_page = ProductPage(driver)
    product_page.open_product_page(0)

    text_button = product_page.get_button_text()
    product_page.click_on_add_to_cart_button()
    text_button_after_first_click = product_page.get_button_text()
    product_page.click_on_remove_button()
    text_button_after_second_click = product_page.get_button_text()

    assert text_button != text_button_after_first_click
    assert text_button == text_button_after_second_click
