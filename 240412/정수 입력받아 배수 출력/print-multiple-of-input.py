n = int(input())

cnt = 0
for i in range(n, 101, 7):
    if i % 7 == 0:
        cnt += 1
        print(i, end=" ")
    if cnt == 5:
        break