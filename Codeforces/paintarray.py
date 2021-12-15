# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    gcdodd = ll[0]
    gcdeven = ll[1]
    for i in range(len(ll)):
        if i%2==0:
            gcdodd = math.gcd(gcdodd,ll[i])
        else:
            gcdeven = math.gcd(gcdeven, ll[i])
    checkodd = True
    for i in range(1,len(ll)):
        if i%2!=0:
            if ll[i]%gcdodd == 0:
                checkodd = False
                break
    if checkodd:
        print(gcdodd)
    else:
        checkeven = True
        for i in range(len(ll)):
            if i%2==0:
                if ll[i]%gcdeven==0:
                    checkeven = False
        if checkeven:
            print(gcdeven)
        else:
            print(0)
