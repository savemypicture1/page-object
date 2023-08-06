

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find(self, locator):
        return self.driver.find_element(*locator)


    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def find_in_element(self, element, locator):
        return element.find_element(*locator)
