# arr = input().split()
# a = int(arr[0])
# b = int(arr[1])

# print(max(a, b) - min(a, b))

inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 출력
if a > b:
	print(a - b)
if a <= b:
	print(b - a)