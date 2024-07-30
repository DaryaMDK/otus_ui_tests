from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        return self.browser.find_element(*locator)

    def wait_for_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
