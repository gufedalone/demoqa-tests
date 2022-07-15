from selene import have, command
from selene.support.shared import browser
from model.controls.table import TableRow
from model.controls.datepicker import DatePicker
from model.controls.dropdown import Dropdown
from model.controls.tags_input import TagsInput
from utils.paths import resource


class StudentRegistrationForm:

    def __init__(self):
        self.birth_date = DatePicker(browser.element('#dateOfBirthInput'))
        self.subjects_ = TagsInput(browser.element('#subjectsInput'))
        self.states = Dropdown(browser.element('#state'))
        self.cities = Dropdown(browser.element('#city'))

    def fill_first_name(self, student_name: str):
        browser.element('#firstName').type(student_name)
        return self

    def fill_last_name(self, student_last_name):
        browser.element('#lastName').type(student_last_name)
        return self

    def fill_email(self, student_email):
        browser.element('#userEmail').type(student_email)
        return self

    def check_gender(self, student_gender):
        browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text(student_gender)).click()

    def fill_mobile_phone(self, student_phone):
        browser.element('#userNumber').type(student_phone)
        return self

    def set_birth_date(self, student_birth_date):
        self.birth_date.add(student_birth_date)
        return self

    def add_subjects(self, *names):
        for name in names:
            self.subjects_.add(name)
        return self

    def check_hobbies(self, *hobbies):
        for hobby in hobbies:
            browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, image):
        browser.element('#uploadPicture').send_keys(resource(image))
        return self

    def fill_current_address(self, student_address):
        browser.element('#currentAddress').type(student_address).perform(command.js.scroll_into_view)
        return self

    def choose_state(self, state_name):
        self.states.select(option=state_name)
        return self

    def choose_city(self, city_name):
        self.cities.select(option=city_name)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self


class RegisteredUser:

    def __init__(self):
        self.full_name = TableRow(0)
        self.email = TableRow(1)
        self.gender = TableRow(2)
        self.mobile = TableRow(3)
        self.date_of_birth = TableRow(4)
        self.subjects = TableRow(5)
        self.hobbies = TableRow(6)
        self.picture = TableRow(7)
        self.address = TableRow(8)
        self.location = TableRow(9)
