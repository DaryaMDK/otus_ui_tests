import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminPage(BasePage):
    def open_admin_catalog_panel(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.browser.get(url)

    @allure.step("Fill general tab")
    def fill_general_tab(self, product_name, meta_tag_title):
        self.logger.info(f"Fill general tab with: {product_name}, {meta_tag_title}")
        self.find_element(By.XPATH, "//*[@aria-label='Add New']").click()
        self.wait_for_element(By.CLASS_NAME, "card-header")
        self.find_element(By.ID, "input-name-1").send_keys(product_name)
        self.find_element(By.ID, "input-meta-title-1").send_keys(meta_tag_title)
        self.find_element(By.XPATH, "//*[@aria-label='Save']").click()

    @allure.step("Fill data tab")
    def fill_data_tab(self, model):
        self.logger.info(f"Fill data tab with: {model}")
        self.find_element(By.XPATH, "//a[normalize-space()='Data']").click()
        self.wait_for_element(By.XPATH, "//legend[normalize-space()='Model']")
        self.find_element(By.ID, "input-model").send_keys(model)

    @allure.step("Fill seo tab")
    def fill_seo_tab(self, keyword):
        self.logger.info(f"Fill seo tab with: {keyword}")
        self.find_element(By.XPATH, "//a[normalize-space()='SEO']").click()
        self.wait_for_element(By.CLASS_NAME, "alert alert-info")
        self.find_element(By.ID, "input-keyword-0-1").send_keys(keyword)

    @allure.step("Get success alert")
    def get_alert_success(self):
        self.logger.info(f"Waiting alert: {self}")
        return self.wait_for_element(By.XPATH, "//*[@class='alert alert-success alert-dismissible']")

    @allure.step("Delete one product")
    def delete_product(self):
        self.find_element(By.XPATH, "//*[@class='form-check-input'][5]").click()
        self.find_element(By.XPATH, "//*[@aria-label='Delete']").click()
