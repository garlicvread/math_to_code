# Create a method for a vector, and initiate it


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 1. Define a vector to return its location value

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)


# 2. Using the vector class, initiate vec1 as x=1, y=1, vec2 as x=2, y=3

vec1 = Vector(1, 1)
vec2 = Vector(2, 3)


# 3. Print vec1, vec2

print(vec1)
print(vec2)
