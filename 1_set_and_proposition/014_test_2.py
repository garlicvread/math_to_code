# 1. 반복문, 조건문을 이용하여 100 이하의 짝수를 원소로 갖는 집합 형성
# 2. union함수를 사용하여 union객체에 even_under_100와 odd_under_100의 합집합을 저장하고 출력

def make_even_under_100():
    even_under_100 = set({})
    
    for i in range(1, 101):
        if i % 2 == 0:
            even_under_100.add(i)
            
    return(even_under_100)
    
    
def make_odd_under_100():
    odd_under_100 = set({})
    
    for i in range(1, 101):
        if i % 2 != 0:
            odd_under_100.add(i)
            
    return(odd_under_100)


even = set(make_even_under_100())
odd = set(make_odd_under_100())

# print(even)
# print(type(even))

union = even.union(odd)
print(union)
