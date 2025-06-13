import math

class Shape:
    def calculate_area(self):
        return

class Rectangle(Shape):# Подкласс Rectangle
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):# Подкласс Circle
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
        
rect = Rectangle(length=5, width=3)
circ = Circle(radius=4)

print(rect.calculate_area())
print(circ.calculate_area())
