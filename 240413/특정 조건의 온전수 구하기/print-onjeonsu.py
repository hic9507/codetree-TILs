n = int(input())

# 조건: if i % 2 == 0 and (i % 10 == 5 and i % 3 == 0 and i % 9 != 0
# 온전수 : 위 조건에 not 연산

for i in range(1, n+1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        continue
    
    print(i, end=" ")