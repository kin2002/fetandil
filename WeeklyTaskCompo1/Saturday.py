from WeeklyTaskInheritance1.Day import  *

class Saturday(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Saturday',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('G It is the 7th day of the week')
    def daily_action2(self):
        print('H It is the 7th day of the week')
