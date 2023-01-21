a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

y = 3
x = 6
print(x + y)

z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)

my_list = [1, 2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print(fun(0,3))

x = 2
y = 3
x = x % y
x = x % y
y = y % x
print(y)

x = float(2)
y = float(4)
print(y ** (1 / x))

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
for x in dct.keys():
    print(dct[x][1], end="")

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))

def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))

x = 1 // 5 + 1 / 5
print(x)

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v)

try:
    value = 0
    print(int(value)/len(value))
except ValueError:
    print("Bad input..")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("very bery bad...")
except:
    print("Boo!...")

print("a", "b", "c", sep="sep")

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
for x in dct.keys():
    print(dct[x][1], end="")

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v)

def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))