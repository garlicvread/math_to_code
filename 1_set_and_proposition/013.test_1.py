# Generate a function that can make a set with elements of odd numbers under 100.

def make_odd_under_100():
    odd_under_100 = set({})
    
    for i in range(1, 101):
        if i % 2 != 0:
            odd_under_100.add(i)
            
    print(odd_under_100)
    
    
make_odd_under_100()
