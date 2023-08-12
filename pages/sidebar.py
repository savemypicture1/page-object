from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains


class Sidebar(BasePage):
    SIDEBAR = (By.CSS_SELECTOR, ".bm-menu-wrap")
    BURGER_MENU = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    X_BUTTON = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    ITEMS = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    ABOUT = (By.CSS_SELECTOR, "#about_sidebar_link")
    LOGOUT = (By.CSS_SELECTOR, "#logout_sidebar_link")
    RESET_APP_STATE = (By.CSS_SELECTOR, "#reset_sidebar_link")


    def is_sidebar_displayed(self):
        sidebar = self.find(self.SIDEBAR)
        return sidebar.get_attribute("aria-hidden")


    def click_on_burger_menu(self):
        self.find(self.BURGER_MENU).click()


    def click_on_x_button(self):
        wait = WebDriverWait(self.driver, 15)
        x_button = self.find(self.X_BUTTON)
        wait.until(EC.element_to_be_clickable(x_button)).click()


    def close_sidebar_by_esc(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.ESCAPE)
        action_chains.perform()


    def click_on_items(self):
        self.find(self.ITEMS).click()


    def click_on_about(self):
        self.find(self.ABOUT).click()


    def click_on_logout(self):
        self.find(self.LOGOUT).click()


    def click_on_reset_app_state(self):
        self.find(self.RESET_APP_STATE).click()
