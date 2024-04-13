n = int(input())
cnt = 0

#### for문
# for i in range(1, n+1):
#     n //= i
#     cnt += 1
#     if n <= 1:
#         print(cnt)
#         break

#### while문
while n >= 1:
    cnt += 1
    n //= cnt
print(cnt)