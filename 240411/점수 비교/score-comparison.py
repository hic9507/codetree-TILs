arr0 = input().split()
arr1 = input().split()
a_math = int(arr0[0])
a_eng = int(arr0[1])

b_math = int(arr1[0])
b_eng = int(arr1[1])

# if a_math > b_math and a_eng > b_eng:
#     print(1)
# else:
#     print(0)
print(1 if a_math > b_math and a_eng > b_eng else 0)