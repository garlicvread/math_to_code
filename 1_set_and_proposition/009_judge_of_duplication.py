# myset 객체에 원소 4를 두 번 추가한 후 출력
# 실행결과: {1, 2, 3, 4, 5, 6}

myset = set({1, 2, 3})

myset.add(4)
myset.add(5)
myset.add(6)

myset.add(4)
myset.add(4)

print(myset)
