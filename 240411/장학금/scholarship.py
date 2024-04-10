arr = input().split()
a, b = int(arr[0]), int(arr[1])

if a >= 90 and b >= 95:
    print(100000)
elif a >= 90 and 90 <= b and b < 95:
    print(50000)
else:
    print(0)