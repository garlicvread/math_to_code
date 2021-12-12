# 1. 100 이하의 홀수를 원소로 하는 집합 형성

def make_odd_under_100():
    odd_under_100 = set({})
    
    for i in range(1, 101):
        if i % 2 != 0:
            odd_under_100.add(i)
            
    print(odd_under_100)
    
    
make_odd_under_100()
