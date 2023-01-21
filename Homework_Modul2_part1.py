

#Task 1
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.
n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
n3 = int(input('Enter number 3: '))
command = str(input('Enter command: [+], [*] :' ))
if command == '+' :
    result = n1+n2+n3
elif command == '*' :
    result = n1*n2*n3
print(result)

##Task 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
n3 = int(input('Enter number 3: '))
command = str(input('Enter command: [min], [max], [arifm_mean] :' ))
if command == 'min' :
    if n1 <= n2 and n1<=n3 :
        result = n1
    elif n2<=n1 and n2<=n3 :
        result = n2
    elif n3<=n2 and n3<=n1 :
        result = n3
elif command == 'max' :
    if n1 >= n2 and n1>=n3 :
        result = n1
    elif n2>=n1 and n2>=n3 :
        result = n2
    elif n3>=n2 and n3>=n1 :
        result = n3
elif command == 'arifm_mean' :
    result = (n1+n2+n3)//3
print(result)

##task_3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.
metr = int(input('Enter metr : '))
command = str(input('Enter command: [yard], [inch], [mi] :' ))
if command == 'yard' :
    result = metr*1.094
elif command == 'inch' :
    result = metr*39.37
elif command == 'mi' :
    result = metr/1609
print(result)


