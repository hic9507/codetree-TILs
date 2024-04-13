##### 방법 1.
# n = int(input())
# a = 0

# while True:
#     if 2**a == n:
#         print(a)
#         break
#     a += 1

##### 방법 2.
n = int(input())
x = 1
cnt = 0

while True:
    if n == x:
        print(cnt)
        break
    x *= 2
    cnt += 1