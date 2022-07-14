from selene import have, command
from selene.support.shared import browser
from model.controls.tags_input import TagsInput
from model.controls.dropdown import Dropdown
from utils.paths import resource
from model.controls.datepicker import DatePicker
from model.controls.table import Table
from model.preconditions import given_opened_registration_form


def test_registration_form():
    given_opened_registration_form()

    # WHEN
    browser.element('#firstName').type('Vlad')
    browser.element('#lastName').type('K')
    browser.element('#userEmail').type('test@mail.qa')

    gender_group = browser.element('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_of_birth.add('10.10.2000')
    '''
    # OR:
    date_of_birth.select('2000', 'October', '10')
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


