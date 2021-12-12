# relative prime/coprime: 서로소
# intersection 객체에 두 집합의 교집합을 저장하고, 이를 활용해 교집합 원소의 개수 여부에 따라 서로소인지 판단하는 결과값 작성

def is_coprime(s1, s2):
    intersection = s1.intersection(s2)
    
    if intersection == 0:
        return False
    else:
        return True

set4 = set({1, 2, 3})
set5 = set({5, 6, 7})
print(is_coprime(set4, set5))
