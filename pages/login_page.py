from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")




    def click_login_button(self):
        return self.find(self.LOGIN_BUTTON).click()


    def enter_username(self, username):
        self.send_keys(self.USER_NAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    # def find_username_field(self):
    #     return self.find(self.USER_NAME)
    #
    # def find_password_field(self):
    #     return self.find(self.PASSWORD)



