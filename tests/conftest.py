import allure
from selene.support.shared import browser
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DEFAULT_REMOTE_DRIVER = 'selenoid.autotests.cloud'

with allure.step('Browser Management'):
    @pytest.fixture(scope='function', autouse=True)
    def browser_management(request):
        remote_driver = request.config.getoption('--remote_driver')
        remote_driver_option = remote_driver if remote_driver != "" else DEFAULT_REMOTE_DRIVER
        options = Options()

        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        options.capabilities.update(selenoid_capabilities)

        browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
        browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
        browser.config.hold_browser_open = (
                os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
        )
        browser.config.timeout = float(os.getenv('selene.timeout', '3'))
        browser.config.driver = webdriver.Remote(
            command_executor=f"https://user1:1234@{remote_driver_option}/wd/hub",
            desired_capabilities=selenoid_capabilities
        )



def pytest_addoption(parser):
    parser.addoption(
        '--remote_driver',
        default='selenoid.autotests.cloud'
    )
