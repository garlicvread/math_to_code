"""
The subtraction calculation for vectors is required to subtract one vector from another.
Subtraction of vectors returns the subtraction of each vector element.
So, subtraction of location values of the second x from the first x, and the second y from the first y,
and return the outcome of those means subtraction of vectors.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# You can subtract the two vectors with the minus method. 'minus' method is defined as the follow.
# 1. Define minus method.

    def minus(self, other):
        return Vector(self.x - other.x, self.y - other.y)


# 2. Add vec1 and vec2 then input the return to vec3, and print vec3

vec1 = Vector(1, 1)
vec2 = Vector(2, 3)
vec3 = vec1.minus(vec2)

print(vec3)
