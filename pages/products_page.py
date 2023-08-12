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

    CARD_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_primary")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn_secondary")


    def get_page_title(self):
        return self.find(self.TITLE_PAGE)


    def get_all_card_titles(self):
        titles = []
        for element in self.get_all_cards():
            title = self.find_in_element(element, self.PRODUCT_CARD_TITLE)
            titles.append(title.text)

        return titles


    def get_current_title(self, number):
        current_card = self.get_current_card(number)

        return self.find_in_element(current_card, self.PRODUCT_CARD_TITLE)


    def get_all_card_prices(self):
        prices = []
        for element in self.get_all_cards():
            price = self.find_in_element(element, self.PRODUCT_CARD_PRICE)
            prices.append(price.text[1:])

        return prices


    def get_current_price(self, number):
        current_card = self.get_current_card(number)

        return self.find_in_element(current_card, self.PRODUCT_CARD_PRICE).text


    def get_current_desc(self, number):
        current_card = self.get_current_card(number)

        return self.find_in_element(current_card, self.PRODUCT_CARD_DESC).text


    def sort(self, value):
        sort = self.find(self.SORT)
        select = Select(sort)
        select.select_by_value(value)


    def sorted_titles_az(self):
        self.sort(self.SORT_FROM_A_TO_Z)

        return self.get_all_card_titles()


    def sorted_titles_za(self):
        self.sort(self.SORT_FROM_Z_TO_A)

        return self.get_all_card_titles()


    def sorted_prices_from_low_to_high(self):
        self.sort(self.SORT_FROM_LOW_TO_HIGH)

        return self.get_all_card_prices()


    def sorted_prices_from_high_to_low(self):
        self.sort(self.SORT_FROM_HIGH_TO_LOW)

        return self.get_all_card_prices()


    def get_all_cards(self):
        return self.find_all(self.PRODUCT_CARD)


    def get_current_card(self, number):
        return self.get_all_cards()[number]


    def click_on_product_image(self, number):
        current_card = self.get_current_card(number)
        self.find_in_element(current_card, self.PRODUCT_CARD_IMG).click()


    def click_on_product_title(self, number):
        self.get_current_title(number).click()


    def click_on_add_to_cart_button(self, number):
        current_card = self.get_current_card(number)
        self.find_in_element(current_card, self.ADD_TO_CART_BUTTON).click()


    def click_on_remove_button(self, number):
        current_card = self.get_current_card(number)
        self.find_in_element(current_card, self.REMOVE_BUTTON).click()


    def get_current_card_button(self, number):
        current_card = self.get_current_card(number)

        return self.find_in_element(current_card, self.CARD_BUTTON)


    def click_on_current_card_button(self, number):
        self.get_current_card_button(number).click()
