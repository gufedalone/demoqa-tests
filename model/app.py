from selene import have, command
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from model.pages.student_registration_page import StudentRegistrationForm, RegisteredUser
from utils import attach

form = StudentRegistrationForm()
results = RegisteredUser()

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
driver = webdriver.Remote(
    command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    options=options)
browser.config.driver = driver


def open_form_page():
    browser.open('/automation-practice-form')

    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]') \
        .with_(timeout=18).should(have.size_greater_than_or_equal(3)) \
        .perform(command.js.remove)


def add_attachments():
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    browser.quit()
