from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    def open_login_page(self, url):
        self.browser.get(url)

    def login(self, username, password):
        self.find_element(By.ID, 'input-username').send_keys(username)
        self.find_element(By.ID, 'input-password').send_keys(password)
        self.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    def check_dashboard(self):
        return self.wait_for_element(By.XPATH, "//h1[normalize-space()='Dashboard']")

    def logout(self):
        self.find_element(By.XPATH, "//span[normalize-space()='Logout']").click()


class RegisterPage(BasePage):
    xpath_success_registration = "//h1[normalize-space()='Your Account Has Been Created!']"

    def open_register_page(self, url):
        self.browser.get(url)

    def register(self, firstname, lastname, email, password):
        self.find_element(By.ID, 'input-firstname').send_keys(firstname)
        self.find_element(By.ID, 'input-lastname').send_keys(lastname)
        self.find_element(By.ID, 'input-email').send_keys(email)
        self.find_element(By.ID, 'input-password').send_keys(password)
        self.find_element(By.NAME, "agree").click()
        self.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()

    def get_register_success(self):
        return self.wait_for_element(By.XPATH, self.xpath_success_registration)
