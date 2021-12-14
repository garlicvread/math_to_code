'''
# A matrix is important data structure in programming.
# You can print out the content of a matrix by defining a two by two matrix.
# You can define a matrix with the value of each element of the matrix.


# Defining a two by two matrix.

class Matrix:
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.data = [[a11, a12], [a21, a22]]


# Printing out the matrix.

class Matrix:
    def __str__(self):
        return str(self.data[0][0]) + " " + str(self.data[0][1]) + "\n" + str(self.data[1][0]) + " " + str(self.data[1][1]) + "\n"

mat1 = Matrix()

print(mat1)

# The outcome is the same with following.
# 0 0
# 0 0

# This is because you did not enter any value for each element of the matrix.
# Thus, a zero matrix(or null matrix) is created.
'''


# 1. Create a zero matrix 'mat1' using Matrix() class.

class Matrix:
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.data = [[a11, a12], [a21, a22]]

    def __str__(self):
        return str(self.data[0][0]) + " " + str(self.data[0][1]) + "\n" + str(self.data[1][0]) + " " + str(self.data[1][1]) + "\n"

mat1 = Matrix()


# 2. Using Matrix class, create a matrix 'mat2' which has (1, 2, 3, 4) as its elements.

mat2 = Matrix(1, 2, 3, 4)


# 3. Print mat1 and mat2.
#    Outcome:
#    0 0
#    0 0

#    1 2
#    3 4

print(mat1, mat2)
