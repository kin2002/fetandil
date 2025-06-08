from Day import *

class Sunday(Day):

    def __init__(self, type_of_day, month, date):
        super().__init__(type_of_day = type_of_day, month= month, date=date )

    def one_day(self):
        print('It is the first day of the week')

