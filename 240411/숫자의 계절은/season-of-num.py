m = int(input())

# if 3 <= m and m <= 5:
#     print('Spring')
# elif 6 <= m and m <= 8:
#     print('Summer')
# elif 9 <= m and m <= 11:
#     print('Fall')
# else:
#     print('Winter')

### 간결한 코드
if m >= 12 or m <= 2:   # and는 말 안됨. 12 이상이면서 2 이하여야 함.
    print('Winter')
elif m <= 5:
    print('Spring')
elif m <= 8:
    print('Summer')
else:
    print('Fall')