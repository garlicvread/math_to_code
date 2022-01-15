"""
To calculate the sum of an arithmetic sequence, you have 2 options.

First, use an equation that is already defined.
The equation is:
    Sn = n * (2a + (n - 1) * d) / 2
    where 'Sn' is the sum of the sequence from the first argument to n-th argument
          'n' is the number of arguments
          'a' is the first argument
          'd' is the common difference

Second, use the while loop.

What we are going to do are:
1. Using the equation, complete the function 'calculate_arithmetic_sequence_sum'
   that calculates the sum of an arithmetic sequence.

2. Using the while loop, complete the function 'calculate_sequence_sum'
   that calculates the sum of an arithmetic sequence.

3. Print the results from each method, and compare them to check if they are equal.
"""


def create_arithmetic_sequence(a, d, n):
    result = [a]
    """
    # This code is the same with:
    result = []
    result.append(a) 
    """

    for i in range(1, n):
        result.append(a + (i*d))

    return result


# Direction 1: Using the equation
def calculate_arithmetic_sequence_sum(a, d, n):
    return n * (2 * a + (n - 1) * d) / 2


# Direction 2: Using the while loop
def calculate_sequence_sum(a, d, n):
    result = a
    i = 1

    while i < n:
        result += (a + (i*d))
        i += 1

    return result


arithmetic_seq1 = create_arithmetic_sequence(2, 2, 10)

# Direction 3-1: print the results from each method
print(calculate_arithmetic_sequence_sum(2, 2, 10))
print(calculate_sequence_sum(2, 2, 10))


# Direction 3-2: compare the results from each method
print(calculate_sequence_sum(2, 2, 10) == calculate_arithmetic_sequence_sum(2, 2, 10))
