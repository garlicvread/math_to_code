"""
Create a method that returns or modifies the specific position of a matrix.
  1. For returning of specific position of a matrix: 'get' method.
  2. For modifying of specific position of a matrix: 'set' method.
"""


class Matrix:
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.data = [[a11, a12], [a21, a22]]

    def __str__(self):
        return str(self.data[0][0]) + " " + str(self.data[0][1]) + "\n" + str(self.data[1][0]) + " " + str(self.data[1][1]) + "\n"

    # 1. 'get' method: gets row(=i) and column(=j) information from the input,
    #                  then returns the value from that specific position of the matrix.
    def get(self, i, j):
        return self.data[i-1][j-1]

    # 2. 'set' method: gets row(=i) and column(=j) information and the value to save from the input,
    #                  then saves those to the specific position of the matrix.
    def set(self, i, j, v):
        self.data[i-1][j-1] = v


mat2 = Matrix(1, 2, 3, 4)

# 3. Using 'get' method, print out the elements of (1, 1), (1, 2), (2, 1), (2, 2) in sequence from matrix 'mat2'.
# Result
# 1
# 2
# 3
# 4

print(mat2.get(1, 1))
print(mat2.get(1, 2))
print(mat2.get(2, 1))
print(mat2.get(2, 2))


# 4. Using 'set' method, modify the elements of (1, 1), (1, 2), (2, 1), (2, 2) of 'mat2' as 5, 6, 7, 8 respectively.
# Result
# 5 6
# 7 8
mat2.set(1, 1, 5)
mat2.set(1, 2, 6)
mat2.set(2, 1, 7)
mat2.set(2, 2, 8)

print(mat2)
