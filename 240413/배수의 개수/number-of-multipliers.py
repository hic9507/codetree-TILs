th_cnt, fi_cnt = 0, 0

for _ in range(10):
    a = int(input())
    if a % 3 == 0:
        th_cnt += 1
    if a % 5 == 0:
        fi_cnt += 1
print(th_cnt, fi_cnt)