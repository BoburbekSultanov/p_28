# Polymorphism

"""
polymorphism:
    override : ✅        static : ✅
    overload : 👎        dynamic : 👎
"""
from cmath import pi
from itertools import batched


# class Employee:
#     def calculate_salary(self):
#         pass
#
#
# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         return 5000
#
#
# class PartTimeEmployee(Employee):
#     def calculate_salary(self):
#         return 20000


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return pow(self.side, 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


c = Circle(3)
s = Square(4)
t = Triangle(2, 4)

print(c.area())
print(s.area())
print(t.area())
