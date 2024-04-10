# a, b, c = map(int, input().split())

# print(a + b + c)
# print((a + b + c) // 3) # 231 ms

### 2번
lst = list(map(int, input().split()))
print(sum(lst))
print(sum(lst) // len(lst))