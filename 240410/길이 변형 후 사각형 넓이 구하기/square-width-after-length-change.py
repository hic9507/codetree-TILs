arr = input().split()

row = int(arr[0]) # 가로
column = int(arr[1]) # 세로

row += 8
column *= 3
print(row)
print(column)
print(row * column)