n = int(input())

##### 방법 1.
# cnt = n

# for i in range(n*2-1):
#     for j in range(cnt):
#         print('*', end=" ")
#     print()

#     if i < (n*2-1)//2:
#         cnt -= 1
#     else:
#         cnt += 1

##### 방법 2.
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

for i in range(n-1, 0, -1):
    for j in range(n-i+1):
        print("*", end=" ")
    print()