import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    def open_product(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.browser.get(url)

    @allure.step("Get product title")
    def get_product_title(self):
        self.logger.info(f"Get product title: {self}")
        return self.wait_for_element(By.XPATH, "//h1[normalize-space()='iPhone']")

    @allure.step("Add new product")
    def add_product(self):
        self.logger.info(f"Add product item: {self}")
        add_button = self.find_element(By.XPATH, "//*[@class='btn btn-lg btn-inverse btn-block dropdown-toggle']")
        add_button.click()
        return self.find_element(By.CLASS_NAME, "fa-solid fa-cart-shopping")


class CartPage(BasePage):
    @allure.step("Get all items inside cart")
    def get_cart_items(self):
        self.logger.info(f"Get cart items: {self}")
        cart_button = self.find_element(By.XPATH, "//*[@class='btn btn-lg btn-inverse btn-block dropdown-toggle']")
        cart_button.click()
        return self.find_elements(By.CLASS_NAME, "fa-solid fa-cart-shopping")
