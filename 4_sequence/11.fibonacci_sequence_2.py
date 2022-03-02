"""
Let's declare a function that calculate the n'th element of a fibonacci sequence.

In this time, the calculation should be done on a recursive code.


What you need to do are:
1. Define the function 'fibonacci' using conditional statements and recursion.
2. Return n when n < 2.
3. Store the result of the function in the variable 'fib_result'.
"""


def fibonacci(n):
    if n < 2:
        return n
    else:
        fib_result = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_result


print(fibonacci(3))
