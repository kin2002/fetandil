from Friends import *
import random

class Met(Day):

    def __init__(self, healthy_activities, daily_reading):
        super().__init__(type_of_day = 'Met',
                         healthy_activities= healthy_activities,
                         daily_reading=daily_reading)

    def daily_action1(self):
        print('A It is the first person')
    def daily_action2(self):
        print('A It is the first person')

    def special_day(self):
        did_special_day_work = random.random() < 0.50
        if did_special_day_work:
            self.healthy_activities += 2
        print('Met is Holy Day with double blessing ')


