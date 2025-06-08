from days import *

sunday = Day('መስከረም', 1,2025, 'የእለቱ የቅዱሳን', 7, color='violet' )

monday = Day('መስከረም', 2,2025, 'የእለቱ ቅዱሳን', 7, color='indigo' )

tuesday = Day('መስከረም', 3,2025, 'የእለቱ ቅዱሳን', 7, color='blue' )

wednesday = Day('መስከረም', 4,2025, 'የእለቱ የቅዱሳን', 7, color='green' )

thursday = Day('መስከረም', 4,2025, 'የእለቱ የቅዱሳን', 7, color='yellow' )

friday = Day('መስከረም', 6,2025, 'የእለቱ ቅዱሳን', 7, color='orange' )

saturday = Day('መስከረም', 7,2025, 'የእለቱ ቅዱሳን', 7, color='red' )

print(saturday.type_of_day)

print(f'ዛሬ  {sunday.month} {sunday.date} ነው። {sunday.type_of_day} ቀን ስለሆነ ይህን {sunday.healthy_activities} እናድርግ። ')

print(f'ዛሬ  {monday.month} {monday.date} ነው።'
      f'  {monday.type_of_day} ቀን ስለሆነ'
      f' ይህን {monday.healthy_activities} እናድርግ። ')

print(f'ዛሬ  {tuesday.month} {tuesday.date} ነው።'
      f'  {tuesday.type_of_day} ቀን ስለሆነ'
      f' ይህን {tuesday.healthy_activities} እናድርግ። ')


print(f'ዛሬ  {wednesday.month} {wednesday.date} ነው።'
      f'  {wednesday.type_of_day} ቀን ስለሆነ'
      f' ይህን {wednesday.healthy_activities} እናድርግ። ')

print(f'ዛሬ  {thursday.month} {thursday.date} ነው።'
      f'  {thursday.type_of_day} ቀን ስለሆነ'
      f' ይህን {thursday.healthy_activities} እናድርግ። ')

print(f'ዛሬ  {friday.month} {friday.date} ነው።'
      f'  {friday.type_of_day} ቀን ስለሆነ'
      f' ይህን {friday.healthy_activities} እናድርግ። ')

print(f'ዛሬ  {saturday.month} {saturday.date} ነው።'
      f'  {saturday.type_of_day} ቀን ስለሆነ'
      f' ይህን {saturday.healthy_activities} እናድርግ። ')