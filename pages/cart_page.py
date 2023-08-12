from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Cart(BasePage):
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")
    TITLE_PAGE = (By.CSS_SELECTOR, ".title")

    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".back")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout_button")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn_small.cart_button")

    PRODUCTS_IN_CART = (By.CSS_SELECTOR, ".cart_item")
    PRODUCT_TITLE_IN_CART = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_DESC_IN_CART = (By.CSS_SELECTOR, ".inventory_item_desc")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, ".inventory_item_price")


    def get_page_title_text(self):
        return self.find(self.TITLE_PAGE).text


    def click_on_cart_icon(self):
        self.find(self.CART_ICON).click()


    def click_on_contiue_shopping_button(self):
        self.find(self.CONTINUE_SHOPPING_BUTTON).click()


    def click_on_checkout_button(self):
        self.find(self.CHECKOUT_BUTTON).click()


    def click_on_remove_button_in_cart(self, number):
        current_product = self.get_current_product_in_cart(number)

        return self.find_in_element(current_product, self.REMOVE_BUTTON).click()


    def get_all_products_in_cart(self):
        return self.find_all(self.PRODUCTS_IN_CART)


    def get_current_product_in_cart(self, number):
        return self.get_all_products_in_cart()[number]


    def get_current_product_title_in_cart(self, number):
        current_product = self.get_current_product_in_cart(number)

        return self.find_in_element(current_product, self.PRODUCT_TITLE_IN_CART)


    def get_current_desc_in_cart(self, number):
        current_product = self.get_current_product_in_cart(number)

        return self.find_in_element(current_product, self.PRODUCT_DESC_IN_CART).text


    def get_current_price_in_cart(self, number):
        current_product = self.get_current_product_in_cart(number)

        return self.find_in_element(current_product, self.PRODUCT_PRICE_IN_CART).text


    def click_on_product_title_in_cart(self, number):
        self.get_current_product_title_in_cart(number).click()
