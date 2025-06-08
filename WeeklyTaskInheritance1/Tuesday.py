from WeeklyTaskInheritance1.Day import *

class Tuesday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Tuesday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('C It is the 3rd day of the week')
    def daily_action2(self):
        print('C It is the 3rd day of the week')