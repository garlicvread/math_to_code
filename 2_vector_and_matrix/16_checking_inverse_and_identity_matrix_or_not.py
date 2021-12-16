"""
When a matrix satisfies the following condition, it is called as an inverse matrix.

AX = XA = E, where A is a matrix, X is the inverse matrix, E is an identity matrix.

You can get a inverse matrix of two by two matrix, by calculating the following calculation:

When A = a b
         c d

X = (ad-bc)^-1  *  d -b
                  -c  a

ad-bc is called 'determinant'.
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

    def is_identity(self):
        for i in range(len(self.data)):
            if self.data[i][i] != 1:
                return False
        return True

    # Defining 'inverse' method.

    def inverse(self):

        determinant = self.data[0][0]*self.data[1][1] - self.data[0][1]*self.data[1][0]
        print(determinant)

        if determinant == 0:
            return None  # When the determinant does not exist, return None.
        else:  # returns the inverse matrix when it does exist.
            m = (1/determinant)

            # To verify the calculated matrix is an inverse matrix or not,
            # check the multiplication of it and the original matrix becomes an identity matrix.
            return Matrix(m*self.data[1][1], m*(-1)*self.data[0][1], m*(-1)*self.data[1][0], m*self.data[0][0])


mat1 = Matrix(1, 2, 2, 1)
# print('mat1: \n', mat1)


# Caculate the inverse matrix.
inverse = mat1.inverse()
# print('inverse:')
# print(inverse)


# Check the calculated inverse matrix is really a inverse matrix of the original matrix.
identity = mat1.multiply(inverse)
print(identity.is_identity())
