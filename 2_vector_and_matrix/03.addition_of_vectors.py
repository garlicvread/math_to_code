"""
The addition calculation is required to add two vectors.
The addition of vectors returns the addition of each vector element.
So, the addition of location values of each x and y, and the return of the outcome of those means the addition of vectors.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)

    # You can add up the two vectors with the 'add' method. 'add' method is defined as the follow.
    # 1. Define add method.

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)


# 2. Add vec1 and vec2 then input the return to vec3, and print vec3

vec1 = Vector(1, 1)
vec2 = Vector(2, 3)
vec3 = vec1.add(vec2)

print(vec3)
