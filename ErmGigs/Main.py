from ErmGigs.Erm import *
from ErmGigs.Kin import *
from ErmGigs.Leader import *
from ErmGigs.Worker import *

def meeting(d1: Worker, d2: Worker):
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


def leader_meeting(leader: Leader, worker: Worker):
    while leader.healthy_activities > 0 and leader.healthy_activities > 0:
        print("__________")

        worker.special_day()

        print(f' Leader: {leader.healthy_activities} HP left')
        print(f' {worker.get_type_of_day()}: {worker.healthy_activities} HP left')
        worker.daily_action1()
        leader.healthy_activities -= worker.daily_reading
        leader.daily_action1()
        worker.healthy_activities -= leader.daily_reading
    print("__________")

    if leader.healthy_activities > 0:
        print(f'Hero wins!')
    else:
        print(f'{worker.get_type_of_day()} wins!')

erm = Erm(10,1)
kin = Kin(20,3)
leader = Leader(10,1)
tool = Tool('Sword', 15)
leader.tool = tool
leader.equip_tool()

leader_meeting(leader, erm)
