# try:
#     value = input("enter a value: ")
#     print(value/value)
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very b input...")
# except:
#     print("Booo")
import random


#
# f = open('test.txt','wt')
# f.write('Hello World\n')
# f.write('My name is Lyuca\n')
# f.write('My favorite food is pasta')
# f.close()
#
# # f = open('test.txt','rt')
# # print(f.read()) #dont recomendation
# # f.close()
#
# f = open('test.txt','rt')
# print(f.readline())
# print(f.readline())
# f.close()
#
# f = open('test.txt','rt')
# print(f.readlines())
# f.close()

def random_string(length=20,letters=True,numbers=True,spaces=True):
    letters_string = 'abcdefghijklmnopqrstuvwxyz'
    number_string = '0123456789'
    s = ''
    if letters:
        s = s + letters_string
    if numbers:
        s = s + number_string
    if spaces:
        s = s + (' '* (length//5))
    result = ''

    for i in range(length):
        result = result + random.choice(s)

    return result

def random_file(name,height=30,length=20,letters=True,numbers=True,spaces=True):
    name = name + '.txt'
    f = open(name, 'wt')
    for i in range(height):
        f.write(random_string(length,letters,numbers,spaces))
        f.write('\n')
    f.close()
random_file('ex1')

f = open('ex1.txt','rt')
f1 = open('r1.txt', 'wt')
a = f.readline()
while a:
    a = a[:-1]
    l = a.split(' ')
    for elem in l:
        if len(elem) >= 7:
            f1.write(elem)
            f1.write('\n')
    a = f.readline()
f1.close()
f.close()