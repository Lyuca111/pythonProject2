# Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник,
# 2 — вторник и т.д.

day = int(input('Enter number of day : '))
if day == 1 :
    print('Monday')
elif day == 2 :
    print('Tuesday')
elif day == 3 :
    print('Wednesday')
elif day == 4 :
    print('Thursday')
elif day == 5 :
    print('Friday')
elif day == 6 :
    print('Saturday')
elif day == 7 :
    print('Sunday')
else:
    print('Incorrect number')

# Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

month = int(input('Enter number of month : '))
if month == 1 :
    print('Janury')
elif month == 2 :
    print('February')
elif month == 3 :
    print('March')
elif month == 4 :
    print('April')
elif month == 5 :
    print('May')
elif month == 6 :
    print('June')
elif month == 7 :
    print('Jule')
elif month == 8 :
    print('August')
elif month == 9 :
    print('September')
elif month == 10 :
    print('October')
elif month == 11 :
    print('November')
elif month == 12 :
    print('December')
else:
    print('Incorrect number')


# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

n = int(input('Enter number : '))
if n > 0 :
    print('Number is positive')
elif n < 0 :
    print('Number is negative')
elif n == 0 :
    print('Number is equal to zero')

# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.

n1 = int(input('Enter first number : '))
n2 = int(input('Enter second number : '))

if n1 == n2 :
    print('number is equal')
elif n1 > n2 :
    print(n2 , n1)
elif n1 < n2 :
    print(n1 , n2)