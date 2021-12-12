# A needed calculation for vector class is addition.

# Addition of vectors returns the addition of each vector elements.
# So, addition of location values of each x and of y, and return the outcome of those means addition of vectors.

# Add method is defined as the follow.
# You can add up the two vectors with the add method.

# 1. Define add method.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)


# 2. Add vec1 and vec2 then input the return to vec3, and print vec3

vec1 = Vector(1, 1)
vec2 = Vector(2, 3)
vec3 = vec1.add(vec2)

print(vec3)
