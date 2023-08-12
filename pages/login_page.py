from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3")
    ERROR_MSGS = {"invalid_credentials": "Epic sadface: Username and password do not match any user in this service",
                  "locked_user": "Epic sadface: Sorry, this user has been locked out.",
                  "without_credentials": "Epic sadface: Username is required"}


    def click_login_button(self):
        return self.find(self.LOGIN_BUTTON).click()


    def enter_username(self, username):
        self.send_keys(self.USER_NAME, username)


    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)


    def find_error_msg(self):
        return self.find(self.ERROR_MSG)


    def is_login_button_visible(self):
        return self.find(self.LOGIN_BUTTON).is_displayed()
