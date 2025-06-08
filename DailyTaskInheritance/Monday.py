from Day import *

class Monday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Monday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def A(self):
            print('A It is the 1st task of the day')
    def B(self):
        print('B It is the second task of the day')
    def C(self):
        print('C It is the 3rd task of the day')
    def D(self):
        print('D It is the 4th task of the day')
    def E(self):
        print('E It is the 5th task of the day')
    def F(self):
        print('F It is the 6th task of the day')
    def G(self):
        print('G It is the 7th task of the day')
    def H(self):
        print('H It is the 8th task of the day')