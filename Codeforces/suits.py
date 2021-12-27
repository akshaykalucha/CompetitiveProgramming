# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

a=int(input())
b = int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

ec = 0
fc = 0

if f>e:
    while b>0 and c>0 and d>0:
        b-=1
        c-=1
        d-=1
        fc+=f
    while a>0 and d>0:
        a-=1
        d-=1
        ec+=e
    print(ec+fc)

elif e>f:
    while a>0 and d>0:
        a-=1
        d-=1
        ec+=e
    while b>0 and c>0 and d>0:
        b-=1
        c-=1
        d-=1
        fc+=f
    print(ec+fc)
elif e==f:
    while b>0 and c>0 and d>0:
        b-=1
        c-=1
        d-=1
        fc+=f
    while a>0 and d>0:
        a-=1
        d-=1
        ec+=e
    print(ec+fc)