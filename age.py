age = int(input('Введите год'))
print()
if age % 4 == 0 and age % 100 != 0 and age % 400:
    print(age,'год високосный')
else:
    print('год не високосный')
