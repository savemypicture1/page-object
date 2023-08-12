from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Footer(BasePage):
    TWITTER = (By.CSS_SELECTOR, ".social_twitter a")
    FACEBOOK = (By.CSS_SELECTOR, ".social_facebook a")
    LINKEDIN = (By.CSS_SELECTOR, ".social_linkedin a")


    def click_on_twitter(self):
        self.find(self.TWITTER).click()


    def click_on_facebook(self):
        self.find(self.FACEBOOK).click()


    def click_on_linkedin(self):
        self.find(self.LINKEDIN).click()


    def is_twitter_open(self):
        self.click_on_twitter()
        tabs = self.driver.window_handles
        new_tab = tabs[-1]
        self.driver.switch_to.window(new_tab)

        return self.driver.current_url


    def is_facebook_open(self):
        self.click_on_facebook()
        tabs = self.driver.window_handles
        new_tab = tabs[-1]
        self.driver.switch_to.window(new_tab)

        return self.driver.current_url


    def is_linkedin_open(self):
        self.click_on_linkedin()
        tabs = self.driver.window_handles
        new_tab = tabs[-1]
        self.driver.switch_to.window(new_tab)

        return self.driver.current_url
