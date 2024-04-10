first = input().split()
second = input().split()

first_age, first_sex = int(first[0]), first[1]
second_age, second_sex = int(second[0]), second[1]

if (first_age >= 19 and first_sex == 'M') or (second_age >= 19 and second_sex == 'M'):
    print(1)
else:
    print(0)