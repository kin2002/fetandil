"""
-Modules get used all the time throughout programming.
-It helps with creating more files,
with unique purposes, to help with clean maintainable code"""

import Imports.grade_average_service

homework_assignment_grades = {
    'homework 1':85,
    'homework_2':100,
    'homework_3':81,
                     }
Imports.grade_average_service.calculate_homework(
    homework_assignment_grades)