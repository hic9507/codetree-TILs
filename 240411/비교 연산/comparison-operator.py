a, b = map(int, input().split())

#### 삼항연산자
# print(1 if a >= b else 0)
# print(1 if a > b else 0)
# print(1 if b >= a else 0)
# print(1 if b > a else 0)
# print(1 if a == b else 0)
# if a != b:
#     print(1)
# else:
#     print(0)

#### 비교연산자
print(int(a >= b)) # int 없으면 True, False로 출력
print(int(a > b))
print(int(b >= a))
print(int(b > a))
print(int(a == b))
print(int(a != b))