from selene.core.entity import Element
from selene.support.shared import browser


class Table:

    def __init__(self, element: Element = ...):
        self.element = element if element is not ... else browser.element('.table')

    def cells_of_row(self, index):
        return self.element.all('tbody tr')[index].all('td')
