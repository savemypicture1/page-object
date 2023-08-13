from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutOverview(BasePage):
    TITLE_PAGE = (By.CSS_SELECTOR, ".title")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    FINISH_BUTTON = (By.CSS_SELECTOR, "#finish")

    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")
    SUB_TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_subtotal_label")
    FINAL_TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")
    TAX = (By.CSS_SELECTOR, ".summary_tax_label")

    PRODUCTS_IN_CHECKOUT = (By.CSS_SELECTOR, ".cart_item")
    PRODUCT_TITLE_IN_CHECKOUT = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_DESC_IN_CHECKOUT = (By.CSS_SELECTOR, ".inventory_item_desc")
    PRODUCT_PRICE_IN_CHECKOUT = (By.CSS_SELECTOR, ".inventory_item_price")


    def get_page_title_text(self):
        return self.find(self.TITLE_PAGE).text


    def get_sub_total_price(self):
        price = self.find(self.SUB_TOTAL_PRICE).text

        return round(float(price.split("$")[1]), 2)


    def get_final_total_price(self):
        price = self.find(self.FINAL_TOTAL_PRICE).text

        return float(price.split("$")[1])


    def get_tax(self):
        tax = self.find(self.TAX).text

        return float(tax.split("$")[1])


    def counting_of_tax(self):
        prices = self.get_sum_of_products()

        return round(prices / 100 * 8, 2)


    def get_sum_of_products(self):
        products = self.get_all_products_in_checkout()
        prices = 0
        for element in products:
            price = self.find_in_element(element, self.PRODUCT_PRICE_IN_CHECKOUT)
            prices += float(price.text[1:])

        return round(prices, 2)


    def click_on_cancel_button(self):
        self.find(self.CANCEL_BUTTON).click()


    def click_on_finish_button(self):
        self.find(self.FINISH_BUTTON).click()


    def get_total_price(self):
        return self.find(self.TOTAL_PRICE).text


    def get_all_products_in_checkout(self):
        return self.find_all(self.PRODUCTS_IN_CHECKOUT)


    def get_current_product_in_checkout(self, number):
        return self.get_all_products_in_checkout()[number]


    def get_current_product_title_in_checkout(self, number):
        current_product = self.get_current_product_in_checkout(number)

        return self.find_in_element(current_product, self.PRODUCT_TITLE_IN_CHECKOUT)


    def get_current_desc_in_checkout(self, number):
        current_product = self.get_current_product_in_checkout(number)

        return self.find_in_element(current_product, self.PRODUCT_DESC_IN_CHECKOUT).text


    def get_current_price_in_checkout(self, number):
        current_product = self.get_current_product_in_checkout(number)

        return self.find_in_element(current_product, self.PRODUCT_PRICE_IN_CHECKOUT).text


    def click_on_product_title_in_checkout(self, number):
        self.get_current_product_title_in_checkout(number).click()
