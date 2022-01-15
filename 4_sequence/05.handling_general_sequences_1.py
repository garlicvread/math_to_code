"""
For this time, we will create a function that calculates each element of a general sequence.

What we are going to do are:
1. Create a function 'create_sequence' that takes a function and the number of elements as parameters.
   The function 'create_sequence' should return a list of the elements of the sequence.

2. The function 'create_sequence' should return a list
   where each element is the result of applying the function to the element of the sequence.
   For now, we will create a function 'square' which returns n^2 as it receives n as its input.

3. Using the function 'square', create the sequence 'seq1' as a parameter of 'create_sequence' then print it.
"""


def calculate_sequence_sum(sequence):
    sum_of_sequence = 0

    for v in sequence:
        sum_of_sequence += v

    return sum_of_sequence


# Direction 1
def create_sequence(function, number_of_elements):
    sequence = []

    for i in range(1, number_of_elements+1):
        sequence.append(function(i))

    return sequence


# Direction 2
def square(n):
    return n ** 2


# Direction 3
seq1 = create_sequence(square, 10)
print(seq1)
