n = int(input())

satisfied = True

for i in range(1, n+1):
    if n % i == 0:
        satisfied = False
        if n % 1 == 0 and n % n == 0:
            satisfied = True


if satisfied == True:
    print('P')
else:
    print('C')