from model import app
import allure
from allure_commons.types import Severity
from utils import attach


@allure.tag("Sign up")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "gufedalone")
@allure.feature("Student registration")
@allure.story("Check that form is filled correctly")
@allure.link("https://demoqa.com/automation-practice-form", name="TestingForm")
def test_registration_form():
    with allure.step('Open form page'):
        app.open_form_page('https://demoqa.com/automation-practice-form')

    with allure.step('Fill form'):
        app.form.fill_first_name('Vlad')
        app.form.fill_last_name('K')
        app.form.fill_email('test@mail.qa')
        app.form.check_gender('Male')
        app.form.fill_mobile_phone('1234567890')
        app.form.set_birth_date('10.10.2000')
        app.form.add_subjects('Maths', 'Economics')
        app.form.check_hobbies('Sports')
        app.form.upload_picture('test_image.png')
        app.form.fill_current_address('Address street')
        attach.add_screenshot()
        app.form.choose_state('NCR')
        app.form.choose_city('Delhi')
        app.form.submit()

    with allure.step('Check form results'):
        app.results.full_name.should_have('Vlad K')
        app.results.email.should_have('test@mail.qa')
        app.results.gender.should_have('Male')
        app.results.mobile.should_have('1234567890')
        app.results.date_of_birth.should_have('10 October,2000')
        app.results.subjects.should_have('Maths, Economics')
        app.results.hobbies.should_have('Sports')
        app.results.picture.should_have('test_image.png')
        app.results.address.should_have('Address street')
        app.results.location.should_have('NCR Delhi')
