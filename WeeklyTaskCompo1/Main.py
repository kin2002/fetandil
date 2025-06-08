from WeeklyTaskCompo1.Sunday import *
from WeeklyTaskCompo1.Monday import *
from WeeklyTaskCompo1.Tuesday import Tuesday
from WeeklyTaskCompo1.Wednesday import Wednesday
from WeeklyTaskCompo1.Thursday import Thursday
from WeeklyTaskCompo1.Friday import *
from WeeklyTaskCompo1.Saturday import  *

def month(d1: Day, d2: Day):
    d1.daily_action1()
    d2.daily_action1()

    while d1.healthy_activities > 0 and d2.healthy_activities > 0:
        print("__________")
        d1.special_day()
        d2.special_day()
        print(f' {d1.get_type_of_day()}: {d1.healthy_activities} HP left')
        print(f' {d2.get_type_of_day()}: {d2.healthy_activities} HP left')

        d2.daily_action2()
        d1.healthy_activities -= d2.daily_reading
    print("__________")

    if d1.healthy_activities > 0:
        print(f'{d1.get_type_of_day()} wins!')
    else:
        print(f'{d2.get_type_of_day()} wins!')

sunday = Sunday(10,8)
monday = Monday(1,3)

month(sunday,monday)

tuesday = Tuesday(3,12)
wednesday = Wednesday(3,120)
thursday = Thursday(1,3)
friday = Friday(3,12)
saturday = Saturday(3,12)

print(sunday.daily_action1())
print(monday.daily_action1())
print(tuesday.daily_action1())
print(wednesday.daily_action1())
print(thursday.daily_action1())
print(friday.daily_action1())
print(saturday.daily_action1())

