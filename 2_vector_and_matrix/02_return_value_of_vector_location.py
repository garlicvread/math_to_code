# register a method for a vector, and initiate it
# 1. define a vector to return its location value
# 2. using the vector class, initiate vec1 as x=1, y=1, vec2 as x=2, y=3
# 3. print vec1, vec2


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : " + str(self.x) + ", y : " + str(self.y)
