n = int(input())

cnt = 0

##### 방법 1. 조건 한 번에 작성
for i in range(1, n+1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0: ### 평년: i % 100 == 0 and i % 400 != 0 
        cnt += 1
print(cnt)

# for i in range(1, n+1):
#     if i % 4 == 0:
#         if i % 100 == 0:        # 104년은 윤년인데 여기서 막혀서 안됨
#             if i % 400 == 0:
#                 cnt += 1
# print(cnt)