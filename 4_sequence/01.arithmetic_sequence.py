# Arithmetic progression is also called geometric progression.

"""
The sequence of integers 2, 4, 6, 8, 10, ··· is the sequence that is created by
sequentially adding 2 to the first argument.

Likewise, a sequence that is created by sequentially adding a certain constant to the first argument is called
an arithmetic sequence, or an arithmetic progression.

The certain constant number to be added is called 'the common difference', and it is displayed as 'd'.

We can create an arithmetic sequence by using while loop.
At this time, the 'set' type data structure is not good to create a list for an arithmetic sequence.
It is because the common difference can be zero, and the 'set' type data structure cannot handle it.
Thus, we use 'list' type data structure to create an arithmetic sequence.

What we are going to do are:
1. Using list type data structure, create the function 'create_arithmetic_sequence'
   which stores from the first argument to the n-th argument.
   Note that the while loop should be used.

2. Create the list 'arithmetic_seq1' for an arithmetic sequence
   that has 2 as the first argument, and 2 as the common difference.
   The number of arguments is 10.

3. print the length of arithmetic_seq1.
"""


def create_arithmetic_sequence(first_arg=0, common_diff=0, n=10):
    list_temp = []

    while len(list_temp) < n:
        list_temp.append(first_arg)
        first_arg += common_diff

    return list_temp


answer = create_arithmetic_sequence(first_arg=2, common_diff=2, n=10)
print(answer)
print(len(answer))
