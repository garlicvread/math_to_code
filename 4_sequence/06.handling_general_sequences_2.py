"""
For this time, we will use the lambda function to handle various sequences.

Let's assume that we declare the general element(n-th element) 'an' of a sequence as:
    an = 2n^2 + 3n + 4

What we are going to do are:
1. Apply the above formula and 'create_sequence' function below,
   create the sequence 'seq2' that has 20 elements.

2. Print 'seq2'.

3. Using the 'calculate_sequence_sum' function, print the sum of 'seq2'.
"""


def calculate_sequence_sum(sequence):
    summation = 0

    for v in sequence:
        summation += v

    return summation


def create_sequence(func, n):
    temp_list = []

    for i in range(1, n + 1):
        temp_list.append(func(i))

    return temp_list


seq2 = create_sequence(lambda x: 2 * x ** 2 - 3 * x + 4, 20)
print(seq2)
print(calculate_sequence_sum(seq2))
