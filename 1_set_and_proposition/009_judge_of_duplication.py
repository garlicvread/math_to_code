# Add 3 to 'myset' object twice then print the result.
# Result: {1, 2, 3, 4, 5, 6}

myset = set({1, 2, 3})

myset.add(4)
myset.add(5)
myset.add(6)

myset.add(4)
myset.add(4)

print(myset)
