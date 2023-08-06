



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self._wait = WebDriverWait(driver, 5)

    def find(self, locator):
        return self.driver.find_element(*locator)



    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)


