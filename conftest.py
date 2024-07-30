import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ya", "ch", "ff", "sa"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--yadriver", default="E:/drivers/yandexdriver"
    )

    parser.addoption(
        "--url", action="store", default="http://localhost/"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    url = request.config.getoption("--url")

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

    yield driver

    driver.quit()
