"""
Tower of Hanoi

The tower of Hanoi algorithm receives four parameters.
1. n: the number of plates you are going to move.
2. from_rod: the starting rod you start to move a plate.
3. to_rod: the ending rod location.
4. aux_rod: the auxiliary rod location. It helps to move the plates.


The order of moving plates are as follows:
1. Using a recursive function, move n-1 of plates from from_rod to aux_rod.
2. Move the remaining plate from from_rod to to_rod.
3. Using the recursive function, move n-1 of plates from aux_rod to to_rod.


What you are going to do are:

1. Create the function "hanoi" that takes four parameters to solve the tower of Hanoi problem.
2. Input 3 to n, "A" to from_rod, "B" to to_rod, "C" to aux_rod then run the function.


Expected Output:
1st move: A -> C
2nd move: A -> B
3rd move: C -> B
4th move: A -> C
5th move: B -> A
6th move: B -> C
7th move: A -> C
"""


def hanoi(n, from_rod, to_rod, aux_rod):
    """
    :param n: the number of plates you are going to move.
    :param from_rod: the starting rod you start to move a plate.
    :param to_rod: the ending rod location.
    :param aux_rod: the auxiliary rod location. It helps to move the plates.
    """
    if n == 1:
        print(f"Move {n}th plate from {from_rod} to {to_rod}")
    else:
        hanoi(n-1, from_rod, aux_rod, to_rod)
        print(f"Move {n}th plate from {from_rod} to {to_rod}")
        hanoi(n-1, aux_rod, to_rod, from_rod)


n = int(input("Input the number of plates to move: "))
hanoi(n, "A", "C", "B")


# # Alternative Solution
# def hanoi(n, from_rod, to_rod, aux_rod):
#     if n == 1:
#         print(f"Move {n}th plate from {from_rod} to {to_rod}")
#         return
#
#     hanoi(n-1, from_rod, aux_rod, to_rod)
#     print(f"Move {n}th plate from {from_rod} to {to_rod}")
#     hanoi(n-1, aux_rod, to_rod, from_rod)
