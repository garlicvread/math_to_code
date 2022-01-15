"""
A Fibonacci sequence is a sequence that starts with the first element and the second element.
It consists of the first and second elements, then the sum of the two previous elements from the third.

For example, the third element will be the summation of the first element and the second element.
If the first element is 0 and the second element is 1, then the Fibonacci sequence will be:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...]

We will declare a function 'create_fibonacci_sequence' that returns a list of Fibonacci sequence up to the given number.

The usage of the function 'create_fibonacci_sequence' will be:
fibo_seq = create_fibonacci_sequence(10)
print(fibo_seq)  # The output will be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

What we are going to do are:
1. Create the function 'create_fibonacci_sequence' that returns a list of a fibonacci sequence.
2. Store the result to a variable 'fibo_seq' then print the result.
"""


def create_fibonacci_sequence(n):
    sequence = [0, 1]

    for i in range(n-2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


fibo_seq = create_fibonacci_sequence(10)
print(fibo_seq)
