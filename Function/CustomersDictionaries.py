"""Customers Dictionaries"""
from asyncio import ALL_COMPLETED


def user_dictionary ( firstname, lastname, username, phone, address):
    created_user_dictionary ={
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "phone": phone,
        "user_address": address

    }
    return created_user_dictionary

solution_dictionary = user_dictionary(firstname="Kin", lastname="G",
                                      username="KinG", phone="3017654321", address="MD")

for x in solution_dictionary:
    print(f" Student {x}")

print(solution_dictionary)