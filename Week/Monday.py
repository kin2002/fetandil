from Day import *

class Monday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Monday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('B It is Kinfe')
    def daily_action2(self):
        print('C It is the 2nd day of the week')