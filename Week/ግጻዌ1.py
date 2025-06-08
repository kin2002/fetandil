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

ግጻዌ = {'እሑድ': 'አበገደሀወዘሐ','ሰኞ':'ጠ', 'ማክሰኞ': 'የከለ','ረቡእ':'መነሰ',
           'ሀሙስ':'ዐፈጸ','ዓርብ':'ቀረሠ','ቅዳሜ':'ተ'}

for x,y in ግጻዌ.items():
    print(f" የእለቱ {x, y}")
for x in ግጻዌ:
        print(x)
