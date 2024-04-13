##### 정수를 문자열로 >> 자릿수가 많아지면 문제될 수 있음
# n = int(input())

# for i in range(1, n+1):
#     if (i % 3 == 0) or ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
#         print(0, end=" ")
#     else:
#         print(i, end=" ")

##### 수학적 접근: 특정 숫자를 포함하는 수는 10으로 나누었을 때 몫이나 나머지가 특정 숫자인 것.
n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end=" ")
    elif i // 10 == 9 or i % 10 == 9:
        print(0, end=" ")
    elif i // 10 == 6 or i % 10 == 6:
        print(0, end=" ")
    elif i // 10 == 3 or i % 10 == 3:
        print(0, end=" ")
    else:
        print(i, end=" ")