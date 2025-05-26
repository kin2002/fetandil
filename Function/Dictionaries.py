"""Dictionaries"""
user_dictionary = {    "username": 'codewithking',    'name': 'King',    'age': 35 }

# del user_dictionary
user_dictionary.pop("age")
user_dictionary["married"] = True
# user_dictionary.clear()
print(user_dictionary.get("name"))
print(user_dictionary)
print(len(user_dictionary))
print(user_dictionary)
for x in user_dictionary:
    print(x)

for x,y in user_dictionary.items():
        print(x,y)