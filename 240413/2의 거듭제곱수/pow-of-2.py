n = int(input())
a = 0

while True:
    if 2**a == n:
        print(a)
        break
    a += 1