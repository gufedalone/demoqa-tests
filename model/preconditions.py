from selene import command, have
from selene.support.shared import browser


def given_opened_registration_form():
    browser.open('/automation-practice-form')

    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')\
        .with_(timeout=10).should(have.size_greater_than_or_equal(3))\
        .perform(command.js.remove)

