from selene.support.shared import browser
import pytest
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.hold_browser_open = (
        os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))


def pytest_addoption(parser):
    parser.addoption(
        '--remote_driver',
        default='selenoid.autotests.cloud'
    )
