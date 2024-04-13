cnt = 0
while True:
    n = int(input())
    
    if n % 2 == 0:
        n //= 2
        cnt += 1
        print(n)

    if cnt == 3:
        break