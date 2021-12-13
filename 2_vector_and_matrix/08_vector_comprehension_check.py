import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)

    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def normalize(self):
        v_len = self.length()

        return Vector(self.x / v_len, self.y / v_len)


# 1. Create a vector with elements of x = 5, y = 4.
vec = Vector(5, 4)

# 2. Input te size of vec element to an element 'vec_length'.
vec_length = vec.length()

# 3. Normalize the object 'vec', and input it to an object 'vec_normalized'.
vec_normalized = vec.normalize()

# 4. print 'vec_length' and 'vec_normalized' objects.
print(vec_length)  # 6.4031242374328485
print(vec_normalized)  # x : 0.7808688094430304, y : 0.6246950475544243
