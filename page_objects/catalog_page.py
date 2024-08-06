import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    def open_catalog(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.browser.get(url)

    @allure.step("Get iphone")
    def get_iphone_element(self):
        self.logger.info(f"Get iphone element: {self}")
        return self.wait_for_element(By.XPATH, "//a[normalize-space()='iPhone']")

    @allure.step("Switch currency and price")
    def switch_currency(self, currency, price):
        self.logger.info(f"Switch currency and price: {currency}, {price}")
        self.find_element(By.ID, "form-currency").click()
        self.find_element(By.XPATH, f"//a[normalize-space()='{currency}']").click()
        return self.find_element(By.XPATH, f"//span[normalize-space()='{price}']")
