from selenium.webdriver.common.by import By
from base_page import BasePage


class AdminPage(BasePage):
    def open_admin_panel(self, url):
        self.browser.get(url)

    def fill_general_tab(self, product_name, meta_tag_title):
        self.find_element(By.XPATH, "//*[@aria-label='Add New']").click()
        self.wait_for_element(By.CLASS_NAME, "card-header")
        self.find_element(By.ID, "input-name-1").send_keys(product_name)
        self.find_element(By.ID, "input-meta-title-1").send_keys(meta_tag_title)
        self.find_element(By.XPATH, "//*[@aria-label='Save']").click()

    def fill_data_tab(self, model):
        self.find_element(By.XPATH, "//a[normalize-space()='Data']").click()
        self.wait_for_element(By.XPATH, "//legend[normalize-space()='Model']")
        self.find_element(By.ID, "input-model").send_keys(model)

    def fill_seo_tab(self, keyword):
        self.find_element(By.XPATH, "//a[normalize-space()='SEO']").click()
        self.wait_for_element(By.CLASS_NAME, "alert alert-info")
        self.find_element(By.ID, "input-keyword-0-1").send_keys(keyword)

    def get_alert_success(self):
        return self.wait_for_element(By.XPATH, "//*[@class='alert alert-success alert-dismissible']")

    def delete_product(self):
        self.find_element(By.XPATH, "//*[@class='form-check-input'][5]").click()
        self.find_element(By.XPATH, "//*[@aria-label='Delete']").click()
