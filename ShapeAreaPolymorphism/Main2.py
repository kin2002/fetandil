# Polymorphism in Shapes

from Shape import *

class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius
    def area(self):
        return 3.14 * self.radius**2

class Bar(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

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

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Bar(2,1), Triangle(6, 7), Square(5), Pizza('pepper', 15)]

for shape in shapes:
    print(f'{shape.area()} cm^2')



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