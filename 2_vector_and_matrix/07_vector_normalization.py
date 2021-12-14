# To normalize a vector, you need to divide the elements(x and y) by the size of the vector.
# When you normalize a vector, the vector keeps the direction as before, but the size becomes 1.

# Vector normalize method divide the elements of a vector by its size then returns the result.
# 'normalize' method is defined as following.

import math

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

    # 'self' here refers to itself.
    def length(self):
        # Using self, you can use x and y value of itself.
        return math.sqrt((self.x * self.x) + (self.y * self.y))

# 1. Define vector normalize method.
    def normalize(self):
        v_len = self.length()
        return Vector(self.x / v_len, self.y / v_len)


# 2. Using normalize method, normalize vec2. And then, input the result to the element 'normalized'.
vec1 = Vector(2, 2)
vec2 = Vector(2, 3)

# normalized = vec1.normalize()
# x : 0.5547001962252291, y : 0.8320502943378437
normalized = vec2.normalize()


# 3. Print 'normalized'.
print(normalized)


# 4. Print the length of 'normalized'. Result: 1.0
print(normalized.length())
