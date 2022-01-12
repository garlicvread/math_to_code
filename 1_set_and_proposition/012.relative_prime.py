"""
relative prime/coprime: 서로소

Store the intersection of set1 and set2
then with the number of elements of the intersection,
check if the two sets are relative prime or coprime to each other.
"""


def is_coprime(s1, s2):
    intersection = s1.intersection(s2)
    
    if intersection == 0:
        return False
    else:
        return True


set4 = {1, 2, 3}
set5 = {5, 6, 7}
print(is_coprime(set4, set5))
