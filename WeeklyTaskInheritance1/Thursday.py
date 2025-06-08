from WeeklyTaskInheritance1.Day import *

class Thursday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Thursday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('E It is the 5th day of the week')
    def daily_action2(self):
        print('E It is the 5th day of the week')