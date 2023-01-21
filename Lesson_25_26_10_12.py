f = open('test.txt','wt')
f.write('Hello World!\n')
f.write('My name is Lyuca')
f.close()

f = open('test.txt', 'rt')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('test.txt', 'at')
f.write('Hello World!\n')
f.write('My name is Lyuca\n')
f.close()

import