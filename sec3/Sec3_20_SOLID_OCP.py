# OPEN/CLOSED PRINCIPLE (OCP)
# To add more shapes, we'd need to modify the AreaCalculator class
# by adding more conditional statements. This aproach makes the code
# less flexible and more prone to errors


class AreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return 3.14159 * shape.radius**2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# in the next code in order to follow the ocp principle modifications are made.
# this adheres to the OCP because we can now add more shapes without modifying the
# AreaCalculator class.

from abc import ABC, abstracmethod

class Shape(ABC):
    @abstracmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def are(self):
        return 3.14159 * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class AreaCalculator:
    def area(self, shape):
        return shape.area()


    



