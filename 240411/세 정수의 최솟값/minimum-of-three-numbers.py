a, b, c = map(int, input().split())

# print(min(a, b, c))

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)