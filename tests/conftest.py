from selene.support.shared import browser
import pytest
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
        os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))


'''
@pytest.fixture()
def registration_form_data():
	browser.element('[id=firstName]').type('Vlad').press_tab()
	browser.element('[id=lastName]').type('Kh').press_tab()
	browser.element('[id=userEmail]').type('qa@gu.ru').press_tab()
	browser.element('[id=age]').type('21').press_tab()
	browser.element('[id=salary]').type('2500').press_tab()
	browser.element('[id=department]').type('Legal').press_enter()
'''