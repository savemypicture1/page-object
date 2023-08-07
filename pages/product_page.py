from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, ".inventory_details_back_button")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".inventory_details_name")
    PRODUCT_DESC = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")


    def back_to_products_button_is_visible(self):
        return self.find(self.BACK_TO_PRODUCTS_BUTTON).is_displayed()


    def click_on_back_products_button(self):
        self.find(self.BACK_TO_PRODUCTS_BUTTON).click()


    def get_product_title(self):
        return self.find(self.PRODUCT_TITLE).text


    def get_product_desc(self):
        return self.find(self.PRODUCT_DESC).text


    def get_product_price(self):
        return self.find(self.PRODUCT_PRICE).text
