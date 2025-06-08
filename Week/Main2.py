from Day import *

sunday = Day('መስከረም', 1,2025, 'የእሑድ እለት የቅዱሳን', 2, color='violet' )

monday = Day('መስከረም', 2,2025, 'የሰኞ እለት ቅዱሳን', 3, color='indigo' )

tuesday = Day('መስከረም', 3,2025, 'የማክሰኞ እለት ቅዱሳን', 3, color='blue' )

wednesday = Day('መስከረም', 4,2025, 'የረቡእ እለት የቅዱሳን', 3, color='green' )

thursday = Day('መስከረም', 4,2025, 'የሀሙስ እለት የቅዱሳን', 4, color='yellow' )

friday = Day('መስከረም', 6,2025, 'የዓርብ እለት ቅዱሳን', 4, color='orange' )

saturday = Day('መስከረም', 7,2025, 'የቅዳሜ እለት ቅዱሳን', 1, color='red' )

print(sunday.get_type_of_day())
print(sunday.one_day())
print(monday.two_day())
print(tuesday.three_day())
print(wednesday.four_day())
print(thursday.five_day())
print(friday.six_day())
print(saturday.seven_day())




