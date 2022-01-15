"""
To calculate the sum of a geometric sequence, you have 2 options.

First, use an equation that is already defined.
The equation is:
    Sn = (a * (1 - r^n)) / (1 - r) or (a * (r^n - 1)) / (r - 1)
    where 'Sn' is the sum of the sequence from the first argument to n-th argument
          'n' is the number of arguments
          'a' is the first argument
          'r' is the common ratio

Second, use the while loop.

What we are going to do are:
1. Using the equation, complete the function 'calculate_geometric_sequence_sum'
   that calculates the sum of a geometric sequence.

2. Using the while loop, complete the function 'calculate_sequence_sum'
   that calculates the sum of an arithmetic sequence.

3. Print the results from each method, and compare them to check if they are equal.
"""


def create_geometric_sequence(a, d, n):
    result = [a]

    for i in range(1, n):
        result.append(result[len(result) - 1] * d)

    return result


def calculate_sequence_sum(seq):
    result = 0

    for i in seq:
        result += i

    return result


# Direction 1: Using the equation
def calculate_geometric_sequence_sum(a, r, n):
    return a * (1 - r ** n) / (1 - r)


# Direction 2: Using the while loop
def calculate_geometric_sequence_sum_while(a, r, n):
    # # Variation 1: using list
    # result = a
    # i = 1
    # temp_list = []
    #
    # while i < n:
    #     temp_list.append(result)
    #     result *= r
    #     i += 1
    #
    # for i in temp_list:
    #     result += i
    #
    # return result

    # Variation 2: using a variable to store n-th element
    result = a
    current = a
    i = 1

    while i < n:
        result += current * r
        current *= r
        i += 1

    return result


print(calculate_geometric_sequence_sum(1, 2, 10))
print(calculate_geometric_sequence_sum_while(1, 2, 10))
print(calculate_geometric_sequence_sum(1, 2, 10) == calculate_geometric_sequence_sum_while(1, 2, 10))
