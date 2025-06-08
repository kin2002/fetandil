# Shapes count
from abc import ABC, abstractmethod
from Shape import *

class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius
    def area(self):
        return 3.14 * self.radius**2

class Line(Shape):
    def __init__(self, line):
        self.line = line
    def area(self):
        return self.line

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height *0.5

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

    def area(self):
        return self.side ** 2


shapes = [Circle(2), Line(2), Triangle(2, 3), Square(2)]

for shape in shapes:
    print(f'{shape.area()}cm²')



#
# class Pentagon(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#
# class Hexagon(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#