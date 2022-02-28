"""
Defining and utilizing a recursive function

A recursive function can be utilized in some cases of using for loop.
It is a function that calls itself in the original function itself.

For example, the function in the  following code is a recursive function.

    def recursion_func():
        print("RECURSIVE FUNCTION")
        recursion_func()
    recursion_func()


The output of the above code is:
.
.
.
RECURSIVE FUNCTION
RECURSIVE FUNCTION
RECURSIVE FUNCTION
RecursionError: maximum recursion depth exceeded while calling a Python object


The error (RecursionError) you faced means the code reached the memory limit (or the recursion constraint).


What you are going to do are:
1. Define a recursive function "recursive_sum" that sums up all the numbers from 111 to nnn.
   "n" here is the input.

2. With the function you created, store the calculation from 111 to 333 then print the result.
"""

n = int(input("Enter a number: "))

# recursive function that sums up all the numbers from 111 to 100 * n + 10 * n + 1 * n.

# starting_number = 111
# end_number = 100 * n + 10 * n + 1 * n


starting_number = 111
end_number = 100 * n + 10 * n + 1 * n


def recursive_sum(starting_number, end_number):
    if starting_number != end_number:
        return starting_number + recursive_sum(starting_number + 1, end_number)
    else:
        return starting_number


result = recursive_sum(starting_number, end_number)

print(result)
