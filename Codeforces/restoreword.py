# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')


a = input()
b = input()
zz = a+b
mixed = input()
flag = True
for el in set(zz):
    if len(zz) != len(mixed):
        flag = False
        break
    if mixed.count(el) != zz.count(el):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")