"""
multiplication calculation by float numbers

A needed calculation for vector class is multiplication by float numbers.

multiplication of vectors by float numbers returns the multiplication of each vector element
while the direction of the vector stays the same.
So, the multiplication of location values of x and y of a vector by float number
returns the multiplied location values of x and y of the vector.

The multiply method is defined as the following.
You can multiply each element from a vector with the multiply method.
"""


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

    # 1. Define multiply method.

    def multiply(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)


# 2. Using multiply method, multiply vec1 by the float number inputted,
# then save the result to vec2, and print vec2.

vec1 = Vector(1, 1)
vec2 = vec1.multiply(3)

print(vec2)
