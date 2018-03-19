f = open('in.txt')
for line in f:
    print(repr(line.rstrip()))
x = f.read()
print(repr(x))


f = open('in2.txt', 'a', encoding='utf-8')
lines = ('one', 'two', 'three\n')
f.write('\n'.join(lines))
f.close()
with open('in3.txt', 'r') as f, open('in4.txt', 'w') as w:
    for line in f:
        w.write(line)


with open('in3.txt') as inf, open('in4.txt', 'w') as ouf:
    ouf.write(inf.read()[::-1])


import os

dir_list = []
for current_dir, dirs, files in os.walk('sample'):
    for file in files:
        if file.endswith('.py'):
            dir_list.append(current_dir)
            break
dir_list.sort()
for i in dir_list:
    print(i)
