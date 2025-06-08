"""
For and While Loops
"""

# import datetime
# import time
#
# def my_task():
#     print("Running my weekly task!")
#
# while True:
#     if datetime.datetime.now().weekday() == 0: #Monday is 0
#         my_task()
#         time.sleep(7 * 24 * 60 * 60) # sleep for a week
#     else:
#         time.sleep(60) #Check every minute

my_week = {'Sunday': 'አበገደሀወዘሐ','Monday':'ጠ', 'Tuesday': 'የከለ','Wednesday':'መነሰ',
           'Thursday':'ዐፈጸ','Friday':'ቀረሠ','Saturday':'ተ'}

for x,y in my_week.items():
    print(f" My {x, y}")
for x in my_week:
        print(x)
