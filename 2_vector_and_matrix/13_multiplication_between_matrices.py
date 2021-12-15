"""
Multiplication between matrices

The process of multiplication between matrices is the same with following.

AB = 1 2 * a b = (1*a+2*c) (1*b+2*d)
     3 4   c d   (3*a+4*c) (3*b+4*d)

The multiplication process between two matrices can be defined as multiply.
"""

class Matrix:
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.data = [[a11, a12], [a21, a22]]

    def __str__(self):
        return str(self.data[0][0]) + " " + str(self.data[0][1]) + "\n" + str(self.data[1][0]) + " " + str(self.data[1][1]) + "\n"

    def get(self, i, j):
        return self.data[i-1][j-1]

    def set(self, i, j, v):
        self.data[i-1][j-1] = v

    def add(self, other):
        return Matrix(self.data[0][0] + other.data[0][0], self.data[0][1] + other.data[0][1], self.data[1][0] + other.data[1][0], self.data[1][1] + other.data[1][1])

    def sub(self, other):
        return Matrix(self.data[0][0] - other.data[0][0], self.data[0][1] - other.data[0][1], self.data[1][0] - other.data[1][0], self.data[1][1] - other.data[1][1])

    def multiple(self, multiplier):
        return Matrix(self.data[0][0] * multiplier, self.data[0][1] * multiplier, self.data[1][0] * multiplier, self.data[1][1] * multiplier)

    def multiply(self, other):
        return Matrix(
            (self.data[0][0] * other.data[0][0]) + (self.data[0][1] * other.data[1][0]),
            (self.data[0][0] * other.data[0][1]) + (self.data[0][1] * other.data[1][1]),
            (self.data[1][0] * other.data[0][0]) + (self.data[1][1] * other.data[1][0]),
            (self.data[1][0] * other.data[0][1]) + (self.data[1][1] * other.data[1][1])
        )


# Input the result of multiply between mat3 and mat4 to mul_mat, and print mul_mat.
# Result
# 19 22
# 43 50

mat3 = Matrix(1, 2, 3, 4)
mat4 = Matrix(5, 6, 7, 8)

mul_mat = mat3.multiply(mat4)
print(mul_mat)
