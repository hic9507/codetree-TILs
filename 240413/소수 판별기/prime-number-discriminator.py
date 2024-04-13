n = int(input())

#### 방법 1. for문
# satisfied = True

# for i in range(2, n):
#     if n % i == 0:
#         satisfied = False

# if satisfied == True:
#     print('P')
# else:
#     print('C')

#### 방법 2. while문
satisfied = True
i = 2

while i < n:
    if n % i == 0:
        satisfied = False
    i += 1

if satisfied == True:
    print('P')
else:
    print('C')