import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def open_catalog(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.browser.get(url)

    @allure.step("Get all menu items")
    def get_menu_items(self):
        self.logger.info(f"Get menu items: {self}")
        return self.browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")

    @allure.step("Switch currency and price")
    def check_switch_currency(self, currency, price):
        self.logger.info(f"Switch currency and price: {currency}, {price}")
        self.find_element(By.ID, "form-currency").click()
        self.find_element(By.XPATH, f"//a[normalize-space()='{currency}']").click()
        return self.find_element(By.XPATH, f"//span[normalize-space()='{price}']")

