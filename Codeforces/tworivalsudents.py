# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

from math import *

for _ in range(int(input())):
    n,x,a,b=[int(x) for x in input().split()]
    if int(fabs(a-b))+x<=n-1:
        print(int(fabs(a-b))+x)
    else:
        print(n-1)