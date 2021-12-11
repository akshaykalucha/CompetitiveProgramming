# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
def gcd(a):
    zz = [int(i) for i in str(a)]
    k = sum(zz)
    return math.gcd(a,k)


for _ in range(int(input())):
    n = int(input())
    flag = True
    while flag:
        if gcd(n)>1:
            print(n)
            break
        else:
            n+=1
            