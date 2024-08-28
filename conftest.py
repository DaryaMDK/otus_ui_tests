import datetime
import logging
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--selenoid_url", action="store", default="http://localhost:4444/wd/hub")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    vnc = request.config.getoption("--vnc")
    log_level = request.config.getoption("--log_level")
    selenoid_url = request.config.getoption("--selenoid_url")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    options = None
    capabilities = None

    if browser_name == "chrome":
        options = Options()
        if vnc:
            capabilities = {
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if vnc:
            capabilities = {
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
    else:
        raise ValueError("Unsupported browser")

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options,
    )

    driver.set_window_size(1920, 1080)
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    yield driver

    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
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
