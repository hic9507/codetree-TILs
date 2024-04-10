a = float(input())
b = float(input())

# print('High' if a >= 1.0 and b >= 1.0)
if a >= 1.0 and b >= 1.0:
    print('High')
elif a >= 0.5 and b >= 0.5:
    print('Middle')
else:
    print('Low')