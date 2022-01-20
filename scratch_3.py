n = int(input('Введите любое число'))
i = 1
while i < n:
    if i% 3 == 0:
        print(i)
    i += 1
print('Эти числа кратны 3')