n = int(input())
sum_val, cnt = 0, 0

for _ in range(n):
    a = int(input())
    sum_val += a
    cnt += 1
    
avg_val = sum_val / cnt

print(f"{sum_val} {avg_val:.1f}")