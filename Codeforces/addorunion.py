# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    bitarr = [0]*32
    k=None
    for i in range(len(ll)):
        for j in range(32):
            k = ll[i]>>j
            if k&1:
                bitarr[j]+=1
    a = 0
    for i in range(32):
        if bitarr[i]>1:
            a+=int(math.pow(2,i))
    print(a)