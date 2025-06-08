from MetKin.Met import *
from MetKin.Kin import *


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

sunday = Met(10,8)
monday = Kin(1,3)

month(sunday,monday)

print(sunday.daily_action1())
print(monday.daily_action1())

