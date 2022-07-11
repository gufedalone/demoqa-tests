from selene import have, command
from selene.support.shared import browser
from controls.tags_input import TagsInput
from controls.dropdown import Dropdown
from utils.paths import resource
from controls.datepicker import DatePicker
from controls.table import Table


def given_opened_registration_form():
    browser.open('/automation-practice-form')

    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')\
        .with_(timeout=10).should(have.size_greater_than_or_equal(3))\
        .perform(command.js.remove)


def test_registration_form():
    given_opened_registration_form()

    # WHEN
    browser.element('#firstName').type('Vlad')
    browser.element('#lastName').type('K')
    browser.element('#userEmail').type('test@mail.qa')

    gender_group = browser.element('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    date_of_birth = browser.element('#dateOfBirthInput')
    DatePicker.select(date_of_birth, '2000', 'October', '10')
    '''
    # OR:
    DatePicker.add(date_of_birth, '10 Oct 2000')
    '''

    subjects = TagsInput(browser.element('#subjectsInput'))

    subjects.add('Maths')
    subjects.autocomplete('Ec', to='Economics')

    hobbies = browser.element('#hobbiesWrapper')
    hobbies.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()

    browser.element('#uploadPicture').send_keys(resource('test_image.png'))

    browser.element('#currentAddress').type('Address street').perform(command.js.scroll_into_view)

    Dropdown.select(browser.element('#state'), option='NCR')
    Dropdown.autocomplete(browser.element('#city'), option='Delhi')

    browser.element('#submit').perform(command.js.click)

    # THEN:
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )

    results = Table()
    results.cells_of_row(0).should(have.exact_texts('Student Name', 'Vlad K'))
    results.cells_of_row(1).should(have.exact_texts('Student Email', 'test@mail.qa'))
    results.cells_of_row(2).should(have.exact_texts('Gender', 'Male'))
    results.cells_of_row(3).should(have.exact_texts('Mobile', '1234567890'))
    results.cells_of_row(4).should(have.exact_texts('Date of Birth', '10 October,2000'))
    results.cells_of_row(5).should(have.exact_texts('Subjects', 'Maths, Economics'))
    results.cells_of_row(6).should(have.exact_texts('Hobbies', 'Sports'))
    results.cells_of_row(7).should(have.exact_texts('Picture', 'test_image.png'))
    results.cells_of_row(8).should(have.exact_texts('Address', 'Address street'))
    results.cells_of_row(9).should(have.exact_texts('State and City', 'NCR Delhi'))



