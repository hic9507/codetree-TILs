### 1번
# a, b, c = map(int, input().split())

# print(a + b + c)
# print((a + b + c) // 3) # 231 ms

### 2번
# lst = list(map(int, input().split()))
# print(sum(lst))
# print(sum(lst) // len(lst)) # 113 ms

### 3번
arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# print(a+b+c)
# print(((a+b+c) // 3)) # 131ms

print(f"{a+b+c}")
print(f"{(a+b+c) // 3}")