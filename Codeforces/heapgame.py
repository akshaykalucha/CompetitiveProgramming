# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
a, b, n = map(int, input().split())
flag = True
turn = True

while flag:
    if turn:
        zz = math.gcd(a,n)
        if zz <= n:
            n-=zz
            turn = False
        else:
            flag = False
    else:
        zz = math.gcd(b,n)
        if zz <= n:
            n-=zz
            turn = True
        else:
            flag = False
if turn:
    print(1)
else:
    print(0)