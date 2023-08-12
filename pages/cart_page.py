from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Cart(BasePage):
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link a")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".back")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout_button")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn_small.cart_button")

