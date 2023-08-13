from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Checkout(BasePage):
    TITLE_PAGE = (By.CSS_SELECTOR, ".title")

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")

    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")

    ERROR_MSG = (By.CSS_SELECTOR, "h3")
    CLOSE_ERROR_BUTTON = (By.CSS_SELECTOR, ".error-button")


    def get_page_title_text(self):
        return self.find(self.TITLE_PAGE).text


    def click_on_cancel_button(self):
        self.find(self.CANCEL_BUTTON).click()


    def click_on_close_error_message_button(self):
        self.find(self.CLOSE_ERROR_BUTTON).click()


    def click_on_continue_button(self):
        self.find(self.CONTINUE_BUTTON).click()


    def enter_first_name(self, firstname):
        self.send_keys(self.FIRST_NAME, firstname)


    def enter_last_name(self, lastname):
        self.send_keys(self.LAST_NAME, lastname)


    def enter_postal_code(self, postcode):
        self.send_keys(self.POSTAL_CODE, postcode)


    def find_error_msg(self):
        return self.find(self.ERROR_MSG)


    def is_error_message_present(self):
        try:
            self.find_error_msg()
            return True
        except NoSuchElementException:
            return False
