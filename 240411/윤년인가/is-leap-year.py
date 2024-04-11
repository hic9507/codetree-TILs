y = int(input())

##### 조건 잘 묶기
# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print('true')
# else:
#     print('false')

##### 중첩조건문
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('true')
        else:
            print('false')
    else:
        print('true')
else:
    print('false')