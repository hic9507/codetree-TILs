n = int(input())
cnt2, cnt3, cnt12 = 0, 0, 0

for i in range(n+1):
    if i != 0 and i % 12 == 0:
        cnt12 += 1
    else:
        if i != 0 and i % 3 == 0:
            cnt3 += 1
        elif i != 0 and i % 2 == 0:
            cnt2 += 1

print(cnt2, cnt3, cnt12)