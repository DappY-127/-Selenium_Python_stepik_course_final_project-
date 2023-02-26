import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language for browser")
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument(f"--lang={language}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    browser.quit()