a, b = map(int, input().split())

print(1 if a >= b else 0)
print(1 if a > b else 0)
print(1 if b >= a else 0)
print(1 if b > a else 0)
print(1 if a == b else 0)
if a != b:
    print(1)
else:
    print(0)