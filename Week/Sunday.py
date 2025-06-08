from Day import *

class Sunday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Sunday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('A It is Ermiyas')
    def daily_action2(self):
        print('B It is the first day of the week')
