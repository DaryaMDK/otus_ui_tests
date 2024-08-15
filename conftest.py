import datetime
import logging
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch", choices=["ya", "ch", "ff", "sa"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--yadriver", default="E:/drivers/yandexdriver")
    parser.addoption("--url", action="store", default="http://localhost/")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))
    driver = None

    if browser_name == "ch":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=Service(), options=options)

    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        options.binary_location = "E:/drivers/yandexdriver"
        driver = webdriver.Chrome(
            options=options,
            service=Service(executable_path=yadriver)
        )
    elif browser_name == "sa":
        driver = webdriver.Safari()

    elif browser_name == "eg":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(options=options)

    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.url = url
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "browser" in item.fixturenames:
                web_driver = item.funcargs["browser"]
                screenshot_name = f"screenshots/{item.nodeid.replace('::', '_')}.png"
                web_driver.save_screenshot(screenshot_name)
                allure.attach.file(screenshot_name, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
