from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser......")
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print("Launching Chrome Browser.........")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request .config.getoption("--browser")

    #pytest HTML Report


def pytest_configure(config):
    config._metadata["Project eCommerce"] = 'nop Commerce'
    config._metadata["Module Name"] = 'Customers'
    config._metadata["Tester"] = 'Munish'


# It is hooked for delete/Modify Environment info to HTML Report


@pytest.mark.optlonalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
