from WeeklyTaskInheritance1.Day import *

class Friday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Friday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('F It is the 6th day of the week')
    def daily_action2(self):
        print('F It is the 6th day of the week')