from selenium.webdriver.common.by import By
from base_page import BasePage


class CatalogPage(BasePage):
    def open_catalog(self, url):
        self.browser.get(url)

    def get_iphone_element(self):
        return self.wait_for_element(By.XPATH, "//a[normalize-space()='iPhone']")

    def switch_currency(self, currency, price):
        self.find_element(By.ID, "form-currency").click()
        self.find_element(By.XPATH, f"//a[normalize-space()='{currency}']").click()
        return self.find_element(By.XPATH, f"//span[normalize-space()='{price}']")
