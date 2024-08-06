from selenium.webdriver.common.by import By
from base_page import BasePage


class ProductPage(BasePage):
    def open_product(self, url):
        self.browser.get(url)

    def get_product_title(self):
        return self.wait_for_element(By.XPATH, "//h1[normalize-space()='iPhone']")

    def add_product(self):
        add_button = self.find_element(By.XPATH, "//*[@class='btn btn-lg btn-inverse btn-block dropdown-toggle']")
        add_button.click()
        return self.find_element(By.CLASS_NAME, "fa-solid fa-cart-shopping")


class CartPage(BasePage):
    def get_cart_items(self):
        cart_button = self.find_element(By.XPATH, "//*[@class='btn btn-lg btn-inverse btn-block dropdown-toggle']")
        cart_button.click()
        return self.find_elements(By.CLASS_NAME, "fa-solid fa-cart-shopping")
