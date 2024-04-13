sum_val, cnt = 0, 0

for _ in range(10):
    a = int(input())
    if 0 <= a and a <= 200:
        sum_val += a
        cnt += 1

avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")