from pages.products_page import ProductsPage
from pages.product_page import ProductPage


def test_sort_az(driver, logged_in):
    product = ProductsPage(driver)
    titles = product.sorted_titles_az()

    titles_string = ",".join(titles)
    expected_result = ",".join(sorted(titles))

    assert titles_string == expected_result


def test_sort_za(driver, logged_in):
    product = ProductsPage(driver)
    titles = product.sorted_titles_za()

    titles_string = ",".join(titles)
    expected_result = ",".join(sorted(titles, reverse=True))

    assert titles_string == expected_result


def test_sort_price_from_low_to_high(driver, logged_in):
    product = ProductsPage(driver)
    prices = product.sorted_prices_from_low_to_high()

    prices_string = ",".join(prices)
    expected_result = ",".join(sorted(prices, key=lambda price: float(price)))

    assert prices_string == expected_result


def test_sort_price_from_high_to_low(driver, logged_in):
    product = ProductsPage(driver)
    prices = product.sorted_prices_from_high_to_low()

    prices_string = ",".join(prices)
    expected_result = ",".join(sorted(prices, reverse=True, key=lambda price: float(price)))

    assert prices_string == expected_result


def test_open_product_by_title(driver, logged_in):
    product = ProductsPage(driver)
    product_title = product.get_current_title(0).text
    product_desc = product.get_current_desc(0)
    product_price = product.get_current_price(0)
    product.click_on_product_title(0)

    product_page = ProductPage(driver)
    product_page_title = product_page.get_product_title()
    product_page_desc = product_page.get_product_desc()
    product_page_price = product_page.get_product_price()

    assert product_title == product_page_title
    assert product_desc == product_page_desc
    assert product_price == product_page_price


def test_open_product_by_img(driver, logged_in):
    product = ProductsPage(driver)
    product_title = product.get_current_title(0).text
    product_desc = product.get_current_desc(0)
    product_price = product.get_current_price(0)
    product.click_on_product_image(0)

    product_page = ProductPage(driver)
    product_page_title = product_page.get_product_title()
    product_page_desc = product_page.get_product_desc()
    product_page_price = product_page.get_product_price()

    assert product_title == product_page_title
    assert product_desc == product_page_desc
    assert product_price == product_page_price


def test_card_button(driver, logged_in):
    product = ProductsPage(driver)

    text_button = product.get_current_card_button(0).text
    product.click_on_current_card_button(0)
    text_button_after_first_click = product.get_current_card_button(0).text
    product.click_on_current_card_button(0)
    text_button_after_second_click = product.get_current_card_button(0).text

    assert text_button != text_button_after_first_click
    assert text_button == text_button_after_second_click
