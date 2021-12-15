"""
Multiplication of a matrix by a real number

You can multiply a matrix by a real number.
To do this, you need to multiply each element of the matrix.
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

    # Multiplication of a matrix can be defined as following.
    # The method 'multiple' returns a matrix which has multiplied elements by the multiplier.
    # 'multiplier' here is an inputted real number which will be multiplied to each element of a matrix.
    
    def multiple(self, multiplier):
        return Matrix(self.data[0][0] * multiplier, self.data[0][1] * multiplier, self.data[1][0]  * multiplier, self.data[1][1]  * multiplier)


mat1 = Matrix(1, 2, 3, 4)

# Multiply 'mat1' by the multiplier, 3 in this case, and input the result to matmul3 and print matmul3.
# Result
# 3 6
# 9 12

matmul3 = mat1.multiple(3)
print(matmul3)
