import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.sidebar import Sidebar


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()


@pytest.fixture
def with_open_sidebar(driver):
    sidebar = Sidebar(driver)
    sidebar.click_on_burger_menu()
