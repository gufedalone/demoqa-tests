import time
from selene import have, command
from tests.conftest import browser
from model.pages.student_registration_page import StudentRegistrationForm, RegisteredUser

form = StudentRegistrationForm()
results = RegisteredUser()


def open_form_page(url: str):
    browser.open(url)
    time.sleep(1)
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]') \
        .with_(timeout=10).should(have.size_greater_than_or_equal(3)) \
        .perform(command.js.remove)
