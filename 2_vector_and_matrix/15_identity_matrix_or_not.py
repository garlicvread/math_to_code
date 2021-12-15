"""
Multiplication of a matrix by an identity matrix

A two by two identity matrix looks like this:

1 0
0 1

Let the method that identify the given matrix is an identity matrix or not as 'is_identity'.
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

    def is_same(self, other):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    # define a method that identify the given matrix is identity matrix or not as 'is_identity'.
    def is_identity(self):
        for i in range(len(self.data)):
            if self.data[i][i] != 1:
                return False
        return True


mat1 = Matrix(1, 0, 0, 1)
mat2 = Matrix(1, 2 ,3 ,4)

# Check if the given matrices mat1 and mat2 are identity matrices or not.
result1 = mat1.is_identity()
print(result1)

result2 = mat2.is_identity()
print(result2)
