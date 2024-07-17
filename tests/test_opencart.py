from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    menu = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
    assert len(menu) == 8, "элементов в меню больше"


def test_catalog_page(browser):
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    browser.get(browser.current_url + "/en-gb/apple?route=product/manufacturer.info")
    iphone = browser.find_element(By.XPATH, "//a[normalize-space()='iPhone']")
    wait.until(EC.element_to_be_clickable(iphone))


def test_product_page(browser):
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    browser.get(browser.current_url + "/en-gb/product/apple/iphone")
    product_title = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='iPhone']"))
    )
    assert product_title.is_displayed(), "Страница товара не отображается"


def test_currency_catalog(browser):
    browser.get(browser.current_url + "/en-gb/apple?route=product/manufacturer.info")
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.XPATH, "//a[normalize-space()='£ Pound Sterling']").click()
    cur = browser.find_element(By.XPATH, "//span[normalize-space()='£67.38']")
    assert cur.text == '£67.38', "валюта не поменялась"


def test_currency_main(browser):
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.XPATH, "//a[normalize-space()='$ US Dollar']").click()
    cur = browser.find_element(By.XPATH, "//span[normalize-space()='$602.00']")
    assert cur.text == '$602.00', "валюта не поменялась"


def test_add_product(browser):
    product = browser.find_element(By.XPATH, '//button[@aria-label="Add to Cart"]')
    product.click()
    browser.find_element(By.ID, "cart").click()
    cart_items = browser.find_elements(By.CLASS_NAME, "fa-solid fa-cart-shopping")
    assert len(cart_items) > 0, "Товар не был добавлен в корзину"


def test_login_page(browser):
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    browser.get(browser.current_url + "/administration")
    username = browser.find_element(By.ID, 'input-username')
    username.send_keys("user")
    password = browser.find_element(By.ID, 'input-password')
    password.send_keys("bitnami")
    login = browser.find_element(By.XPATH, "//button[normalize-space()='Login']")
    login.click()
    dashboard = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Dashboard']"))
    )
    assert dashboard.is_displayed(), "Страница не отображается"

    logout = browser.find_element(By.XPATH, "//span[normalize-space()='Logout']")
    logout.click()
    assert login.is_displayed()


def test_register_account(browser):
    wait = WebDriverWait(browser, 7, poll_frequency=1)
    browser.get(browser.current_url + "/index.php?route=account/register")

    firstname = browser.find_element(By.ID, 'input-firstname')
    firstname.send_keys("ivan")
    lastname = browser.find_element(By.ID, 'input-lastname')
    lastname.send_keys("ivanov")
    email = browser.find_element(By.ID, 'input-email')
    email.send_keys("testemail.ru")
    password = browser.find_element(By.ID, 'input-password')
    password.send_keys("test1322")
    agreement = browser.find_element(By.NAME, "agree")
    agreement.click()
    register = browser.find_element(By.XPATH, "//button[normalize-space()='Continue']")
    register.click()
    register_success = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']"))
    )
    assert register_success.is_displayed(), "Страница не отображается"
