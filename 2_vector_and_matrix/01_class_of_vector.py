"""
Python provides 'set' class, but not do so with 'vector' class.
So, users must define 'vector' class and generate vector objects.
A vector can be defined by locations of x and y.
"""


# define a vector object, initialize the location of vector by using the location data of x and y.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
