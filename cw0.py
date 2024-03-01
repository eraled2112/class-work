#problem 1
a = 2 ** 3
b = 3 ** 2
if a > b:
    print(a)
else:
    print(b)

#problem 2
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print('Самое большое число: ', a)
elif b > a and b > c:
    print('Самое большое число: ', b)
else:
    print('Самое большое число: ', c)
if a < b and a < c:
    print('Самое маленькое число: ', a)
elif b < a and b < c:
    print('Самое маленькое число: ', b)
else:
    print('Самое маленькое число: ', c)

#problem 3
a = 17391 % 17
b = 546 % 17
c = 934 % 17
if a < b and a < c:
    print('Отсаток меньше всего от 17391: ', a)
elif b < a and b < c:
    print('Остаток меньше всего от 546: ', b)
else:
    print('Остаток меньше всего от 934: ', c)

# problem 4
x = 13 ** 2
if x < 172:
    print(x ** 2)
else:
    print(x)

# problem 5
a = int(input())
if a % 2 == 0:
    print('Chet')
else:
    print('Nechet')
if a % 3 == 0:
    print('Delitsya')
else:
    print('Nedelitsya')
if a ** 2 < 1000:
    print('Bolshe 1000')
else:
    print('Menshe 1000')

# problem 6
a = int(input())
if 0 < a < 100:
    if 0 < a < 21 or 56 < a < 100:
        print('Allowed diapazon')
    else:
        print('Not allowed diapazon')

# problem 7
a = 23
if a == True:
    print(a)

# problem 8
a = 76
if a < 89:
    if a % 2 == 0:
        if a < 1000:
            print(a)
