"""
The formula to get the size of a vector is the same with followig:
|v| = square root of (x^2 + y^2)

To get the square root of something, math module is needed.
"""

import math


# length function is defined as following.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def minus(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def multiply(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)

    # 'self' refers to itself.
    def length(self):
        # Using self, you can use x and y value of itself.
        return math.sqrt((self.x * self.x) + (self.y * self.y))


# Using length function, you can get the size of vectors.
vec1 = Vector(1, 1)
vec2 = Vector(2, 3)

print(vec1.length())  # 1.4142135623730951
print(vec2.length())  # 3.605551275463989
