from selene import have, command
from tests.conftest import browser
from model.pages.student_registration_page import StudentRegistrationForm, RegisteredUser
from utils import attach

form = StudentRegistrationForm()
results = RegisteredUser()


def open_form_page(url):
    browser.open(url)

    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]') \
        .with_(timeout=20).should(have.size_greater_than_or_equal(3)) \
        .perform(command.js.remove)


def add_attachments():
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    browser.quit()
