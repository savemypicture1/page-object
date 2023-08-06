from pages.products_page import ProductsPage


def test_sort_az(driver, logged_in):
    product = ProductsPage(driver)

    titles = product.sorted_titles(product.SORT_FROM_A_TO_Z)
    titles_string = ",".join(titles)

    expected_result = ",".join(sorted(titles))

    assert titles_string == expected_result


def test_sort_za(driver, logged_in):
    product = ProductsPage(driver)

    titles = product.sorted_titles(product.SORT_FROM_Z_TO_A)
    titles_string = ",".join(titles)

    expected_result = ",".join(sorted(titles, reverse=True))

    assert titles_string == expected_result


def test_sort_price_from_low_to_high(driver, logged_in):
    product = ProductsPage(driver)

    prices = product.sorted_prices(product.SORT_FROM_LOW_TO_HIGHT)

    prices_string = ",".join(prices)
    expected_result = ",".join(sorted(prices, key=lambda price: float(price)))

    assert prices_string == expected_result


def test_sort_price_from_high_to_low(driver, logged_in):
    product = ProductsPage(driver)

    prices = product.sorted_prices(product.SORT_FROM_HIGH_TO_LOW)

    prices_string = ",".join(prices)
    expected_result = ",".join(sorted(prices, reverse=True, key=lambda price: float(price)))

    assert prices_string == expected_result
