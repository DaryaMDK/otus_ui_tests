from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPage(BasePage):
    def open_catalog(self, url):
        self.browser.get(url)

    def get_menu_items(self):
        return self.browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")

    def check_switch_currency(self, currency, price):
        self.find_element(By.ID, "form-currency").click()
        self.find_element(By.XPATH, f"//a[normalize-space()='{currency}']").click()
        return self.find_element(By.XPATH, f"//span[normalize-space()='{price}']")

