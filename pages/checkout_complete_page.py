from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutComplete(BasePage):
    TITLE_PAGE = (By.CSS_SELECTOR, ".title")
    BACK_HOME_BUTTON = (By.CSS_SELECTOR, "#back-to-products")


    def get_page_title_text(self):
        return self.find(self.TITLE_PAGE).text


    def click_on_back_home_button(self):
        self.find(self.BACK_HOME_BUTTON).click()
