from pages.checkout_complete_page import CheckoutComplete
from pages.checkout_overview_page import CheckoutOverview
from pages.products_page import ProductsPage


def test_back_home_button(driver, open_checkout_overview_page_with_product):
    checkout_overview = CheckoutOverview(driver)
    checkout_complete = CheckoutComplete(driver)
    products_page = ProductsPage(driver)
    checkout_overview.click_on_finish_button()
    checkout_complete.click_on_back_home_button()
    result = products_page.get_page_title_text()

    assert result in "Products"
