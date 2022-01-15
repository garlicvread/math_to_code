"""
A sequence that is created by sequentially multiplying a certain constant to the first argument is called
a geometric sequence, or a geometric progression.

The certain constant number to be multiplied is called 'the common ratio', and it is displayed as 'r'.
Note that the common ratio must not be zero.

In this case, the sequence from the first argument to the n-th argument is:
    a, ar, ar^2, ar^3, ... ar^(n-1)

What we are going to do are:
1. Create a function 'create_geometric_sequence' that creates a geometric sequence
   when the first argument, the common ratio, and the number of arguments are given.

2. Create the list 'geometric_seq1' that contains the first 10 elements of the geometric sequence
   which has 1 as the first argument, and 2 as the common ratio.
"""


def create_geometric_sequence(a, r, n):
    result = []

    for i in range(n):
        result.append(a * r ** i)

    return result


geometric_seq1 = create_geometric_sequence(1, 2, 10)
print(geometric_seq1)
