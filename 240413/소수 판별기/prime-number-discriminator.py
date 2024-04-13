n = int(input())

satisfied = True

for i in range(1, n+1):
    if n % 1 == 0 and n % n == 0:
        continue
    else:
        satisfied = False

if satisfied == True:
    print('P')
else:
    print('C')