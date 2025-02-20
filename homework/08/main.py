import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError("u gotta implement this sorry")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Vehicle:
    def describe(self):
        raise NotImplementedError("u gotta implement this sorry")

class Car(Vehicle):
    def describe(self):
        return "this is a car. it has 4 wheels. duh"

class Bike(Vehicle):
    def describe(self):
        return "this is a bike. it has 4 wheels. lol learn to balance"

rect = Rectangle(5, 3)
circle = Circle(4)

print("rectangle area ->", rect.calculate_area())
print("circle area ->", circle.calculate_area())

car = Car()
bike = Bike()

print(car.describe())
print(bike.describe())