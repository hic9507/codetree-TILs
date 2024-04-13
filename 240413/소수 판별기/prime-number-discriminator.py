n = int(input())

satisfied = True

for i in range(2, n+1):
    if n % 1 == 0 and n % n == 0:
        continue
    elif n % i == 0:
        satisfied = False

if satisfied == True:
    print('P')
else:
    print('C')

# i = 1
# satisfied = True

# while i < n:
#     if n % 1 == 0 and n % n == 0:
#         continue
#     if n % 1 == 0 and n % n == 0 and n % i == 0:
#         satisfied = False
#     i += 1

# if satisfied == True:
#     print('P')
# else:
#     print('C')