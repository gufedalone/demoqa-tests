from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


month_number = {'January': '1',
                'February': '2',
                'March': '3',
                'April': '4',
                'May': '5',
                'June': '6',
                'July': '7',
                'August': '8',
                'September': '9',
                'October': '10',
                'November': '11',
                'December': '12'}

class DatePicker:

    def add(self: Element, value: str):
        self.perform(command.js.set_value(value)).press_tab()

    def select(self: Element, year: str, month: str, day: str):
        month_ = month_number[month]
        self.click()
        browser.element(f'.react-datepicker__year-select').element(
            f'[value="{int(year)}"]'
        ).click()
        browser.element(f'.react-datepicker__month-select').element(
            f'[value="{int(month_) - 1}"]'
        ).click()
        browser.element(f'.react-datepicker__day--0{int(day)}').click()



