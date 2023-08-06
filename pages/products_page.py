from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class ProductsPage(BasePage):
    TITLE_PAGE = (By.CSS_SELECTOR, ".title")
    SORT = (By.CSS_SELECTOR, ".product_sort_container")
    SORT_FROM_A_TO_Z = "az"
    SORT_FROM_Z_TO_A = "za"
    SORT_FROM_LOW_TO_HIGH = "lohi"
    SORT_FROM_HIGH_TO_LOW = "hilo"

    PRODUCT_CARD = (By.CSS_SELECTOR, ".inventory_item")
    PRODUCT_CARD_TITLE = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_CARD_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    PRODUCT_CARD_IMG = (By.CSS_SELECTOR, "img.inventory_item_img")
    PRODUCT_CARD_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")

    def get_all_card_titles(self):
        titles = []
        for element in self.get_all_cards():
            title = self.find_in_element(element, self.PRODUCT_CARD_TITLE)
            titles.append(title.text)
        return titles


    def get_all_card_prices(self):
        prices = []
        for element in self.get_all_cards():
            price = self.find_in_element(element, self.PRODUCT_CARD_PRICE)
            prices.append(price.text[1:])
        return prices


    def sort(self, value):
        sort = self.find(self.SORT)
        select = Select(sort)
        select.select_by_value(value)


    def sorted_titles(self, value):
        self.sort(value)
        return self.get_all_card_titles()

    def sorted_prices(self, value):
        self.sort(value)
        return self.get_all_card_prices()


    def get_all_cards(self):
        return self.find_all(self.PRODUCT_CARD)


    def get_current_card(self, number):
        return self.get_all_cards()[number]


    def click_on_product_image(self, number):
        return self.find_in_element(self.get_current_card(number), self.PRODUCT_CARD_IMG).click()
