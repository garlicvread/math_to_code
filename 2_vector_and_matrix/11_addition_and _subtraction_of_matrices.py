"""
Addition and subtraction of matrices

With the two by two Matrix class you created, you can add or subtract two matrices.
By adding up the elements located in the same position of each matrix, you will get the addition of matrices.
By subtracting the elements in the same position, you will get the subtraction of matrices.

You can define functions: for addition, 'add' and for subtraction, 'sub'.
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


    # 1. Define 'sum' function.

    def add(self, other):
        return Matrix(self.data[0][0] + other.data[0][0], self.data[0][1] + other.data[0][1], self.data[1][0] + other.data[1][0], self.data[1][1] + other.data[1][1])


    # 2. Define 'sub' function.

    def sub(self, other):
        return Matrix(self.data[0][0] - other.data[0][0], self.data[0][1] - other.data[0][1], self.data[1][0] - other.data[1][0], self.data[1][1] - other.data[1][1])


mat3 = Matrix(1, 2, 3, 4)
mat4 = Matrix(5, 6, 7, 8)

# 3. Store the result from sum of mat3 and mat4 to 'add_mat', and print it.
# Result
# 6 8
# 10 12

add_mat = mat3.add(mat4)
print(add_mat)

# 4. Store the result from sub of mat3 and mat4 to 'sub_mat', and print it.
# Result
# 4 4
# 4 4

sub_mat = mat4.sub(mat3)
print(sub_mat)
