import allure
from faker import Faker

from page_objects.admin_page import AdminPage
from page_objects.catalog_page import CatalogPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage, CartPage
from page_objects.user_page import LoginPage, RegisterPage


@allure.title('Check menu elements on main page')
def test_main_page(browser):
    main_page = MainPage(browser)
    menu = main_page.get_menu_items()
    assert len(menu) == 8, "элементов в меню больше"


@allure.title('Check switch currency into main page')
def test_currency_main(browser):
    main_page = MainPage(browser)
    main_page.open_catalog(browser.current_url + "/en-gb/apple?route=product/manufacturer.info")
    selected_currency = main_page.check_switch_currency("£ Pound Sterling", "£67.38")
    assert selected_currency == '£67.38', "валюта не поменялась"


@allure.title('Check getting iphone on the product page')
def test_catalog_page(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog(browser.current_url + "/en-gb/apple?route=product/manufacturer.info")
    iphone = catalog_page.get_iphone_element()
    assert iphone.is_displayed(), "iPhone не отображается"


@allure.title('Check product title')
def test_product_page(browser):
    product_page = ProductPage(browser)
    product_page.open_product(browser.current_url + "/en-gb/product/apple/iphone")
    product_title = product_page.get_product_title()
    assert product_title.is_displayed(), "Страница товара не отображается"


@allure.title('Add product to cart')
def test_add_product(browser):
    product_page = ProductPage(browser)
    cart_page = CartPage(browser)
    product_page.add_product()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "Товар не был добавлен в корзину"


@allure.title('Check switch currency into catalog page')
def test_currency_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog(browser.current_url + "/en-gb/apple?route=product/manufacturer.info")
    selected_currency = catalog_page.switch_currency("£ Pound Sterling", "£67.38")
    assert selected_currency == '£67.38', "валюта не поменялась"


@allure.feature("Login")
@allure.story("Successful login")
def test_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page(browser.current_url + "/administration")
    login_page.login("user", "bitnami")
    dashboard = login_page.check_dashboard()
    assert dashboard.is_displayed(), "Страница не отображается"
    login_page.logout()
    assert dashboard.is_displayed()


@allure.feature("Register")
@allure.story("Successful register")
def test_register_account(browser):
    fake = Faker("es_ES")
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.current_url + "/index.php?route=account/register")
    register_page.register(fake.first_name(), fake.last_name(), fake.email(), fake.password())
    register_success = register_page.get_register_success()
    assert register_success.is_displayed(), "Страница не отображается"


@allure.title('Add random product inside admin panel')
def test_add_product_from_admin_panel(browser):
    fake = Faker("es_ES")
    admin_page = AdminPage(browser)
    admin_page.open_admin_catalog_panel(browser.current_url + "/index.php?route=catalog/product")
    admin_page.fill_general_tab(fake.random_company_product(), fake.random_int(100, 1000))
    admin_page.fill_data_tab(fake.word("andsudsweoiwow"))
    admin_page.fill_seo_tab(fake.word("andsudswow"))
    alert_success = admin_page.get_alert_success()
    assert alert_success.is_displayed(), "Warning: Please check the form carefully for errors!"


@allure.title('Delete product inside admin panel')
def test_delete_product(browser):
    admin_page = AdminPage(browser)
    admin_page.open_admin_catalog_panel(browser.current_url + "/index.php?route=catalog/product")
    admin_page.delete_product()
    confirm_alert = browser.switch_to.alert
    confirm_alert.dismiss()
    alert_success = admin_page.get_alert_success()
    assert alert_success.is_displayed(), "Warning: not delete"

