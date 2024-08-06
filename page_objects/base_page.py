import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.wait = WebDriverWait(browser, 10)

    def find_element(self, *locator):
        self.logger.info(f"Finding element by locator: {locator}")
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        self.logger.info(f"Finding elements by locator: {locator}")
        return self.browser.find_element(*locator)

    def wait_for_element(self, *locator):
        self.logger.info(f"Waiting visibility element by locator: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))
