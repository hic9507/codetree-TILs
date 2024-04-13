a, b = map(int, input().split())

for i in range(21):
    m = a // b
    n = a % b
    print(m, end="")

    if i == 0:
        print('.', end="")
    a = (a % b)*10