n = int(input())

for i in range(n):
    for j in range(i*2):
        print(" ", end="")

    for j in range((2 * n) - (2 * i) - 1):# n*2-1, 0, -1 원래 이렇게 함
        print('*', end=" ")
    print()