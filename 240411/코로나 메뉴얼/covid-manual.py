a_arr = input().split()
b_arr = input().split()
c_arr = input().split()

a_flu, a_tem = a_arr[0], int(a_arr[1])
b_flu, b_tem = b_arr[0], int(b_arr[1])
c_flu, c_tem = c_arr[0], int(c_arr[1])

if a_flu == 'Y' and a_tem >= 37:
    if (b_flu == 'Y' and b_tem >= 37) or (c_flu == 'Y' and c_tem >= 37):
        print('E')
    else:
        print('N')

elif b_flu == 'Y' and b_tem >= 37:
    if c_flu == 'Y' and c_tem >= 37:
        print('E')
    else:
        print('N')