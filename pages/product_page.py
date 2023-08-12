from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.products_page import ProductsPage


class ProductPage(BasePage):
    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, ".inventory_details_back_button")

    PRODUCT_TITLE = (By.CSS_SELECTOR, ".inventory_details_name")
    PRODUCT_DESC = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")

    BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_primary")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn.btn_secondary.btn_small")


    def click_on_back_products_button(self):
        self.find(self.BACK_TO_PRODUCTS_BUTTON).click()


    def get_product_title(self):
        return self.find(self.PRODUCT_TITLE).text


    def get_product_desc(self):
        return self.find(self.PRODUCT_DESC).text


    def get_product_price(self):
        return self.find(self.PRODUCT_PRICE).text


    def open_product_page(self, number):
        products_page = ProductsPage(self.driver)
        products_page.click_on_product_title(number)


    def get_button_text(self):
        return self.find(self.BUTTON).text


    def click_on_add_to_cart_button(self):
        self.find(self.ADD_TO_CART_BUTTON).click()


    def click_on_remove_button(self):
        self.find(self.REMOVE_BUTTON).click()
