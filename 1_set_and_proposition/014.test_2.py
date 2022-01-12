# 1. Using for loops and conditional sentences, create sets of even numbers and odd numbers under 100 respectively.
# 2. Using 'union()'function, store the union of the two sets to the object 'union' then print the result.

def make_even_under_100():
    even_under_100 = set({})
    
    for i in range(1, 101):
        if i % 2 == 0:
            even_under_100.add(i)
            
    return even_under_100
    
    
def make_odd_under_100():
    odd_under_100 = set({})
    
    for i in range(1, 101):
        if i % 2 != 0:
            odd_under_100.add(i)
            
    return odd_under_100


even = set(make_even_under_100())
odd = set(make_odd_under_100())

# print(even)
# print(type(even))

union = even.union(odd)
print(union)
