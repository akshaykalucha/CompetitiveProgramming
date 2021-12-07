# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
def isPerfectSquare(x):     
    if(x >= 0):
        sr = math.sqrt(x)
        return ((sr*sr) == float(x))
    return False


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    flag = False
    for i in range(len(ll)-1):
        currprod = ll[i]
        nextlst = ll[i+1:]
        for j in range(len(nextlst)):
            currprod*=nextlst[j]
            if isPerfectSquare(currprod)==False:
                flag=True
                break
    if flag:
        print("YES")
    else:
        print("NO")
        