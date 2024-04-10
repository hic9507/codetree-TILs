# a, b = map(int, input().split())

# print(a+b, (a+b)/2)

lst = list(map(int, input().split()))
print(f"{sum(lst)} {sum(lst)/len(lst)}")