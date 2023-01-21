import random

maximum = 'a'
minimum = 'a'

# a = 0
# while a != 7:
#     a = int(input('Enter number :'))
#     if maximum != 'a':
#         if a > maximum and a != 7:
#              maximum = a
#     elif maximum == 'a':
#         maximum = a
#     if minimum
#     if a < minimum and a != 7:
#         minimum = a
#
# print(minimum, maximum)
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def list_max(l):
#     maximum = l[0]
#     minimum = [0]
#     for elem in l:
#         if elem > maximum:
#             maximum = elem
#         if elem < minimum:
#             minimum = elem
#
#     return maximum
#
# import random
# def suma_function(l):
#     suma_ch = 0
#     suma_nch = 0
#     suma_pol = 0
#     suma_otr = 0
#     for elem in l:
#         if elem % 2 == 0:
#             suma_ch = suma_ch + elem
#         elif elem % 2 != 0:
#             suma_nch = suma_nch + elem
#         elif elem > 0:
#             suma_pol = suma_pol + elem
#         elif elem < 0:
#             suma_otr = suma_otr + elem
#             return (suma_ch, suma_nch, suma_pol, suma_otr)
# l = [random.randint(-20, 25) for i in range(10)]
# print(l)
# print(suma_function(l))
#
# def found(l, num):
#     if num in l:
#         return True
# num = 9
# l = [-14, 9, 38, -45, 25, 9, 9, -29, 55]
# print(found(l, num))
#
# def factorial(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#     return f
# print(factorial(5))
# print(factorial(6))
#
# def sum(a, b, c): #упорядоченные аргументы
#     return a +b +c
# print(sum(2, 3, 4))

def sum(a, b, c, d=5, e=6): #аргументы по умолчанию
    return a +b +c+d+e
print(sum(2, 3, 4))


# def my_range(start, finish=int(), step=1):
#     if not finish:
#         finish = 0
#     start, finish = finish, start
# l = []
# if step > 0:
#     while start < finish:
#         l.append(start)
#         start = start + step
# elif step < 0:
#     while start > finish:
#         l.append(start)
#         start = start + step
#     return l


def per (a, b, c, d=0, e=0):
    return a +b +c + d + e
print('perimetre', per(2, 3, 4))

def nangle(*args): #неупорядоченные аргументы
    p = 0
    for elem in args:
        p = p + elem
    return p
print(nangle(1,2,3))
print(nangle(1,2,3,4,5,6,7,8,9,10,11))