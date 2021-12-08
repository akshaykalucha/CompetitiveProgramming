# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    flag = True
    for i in range(len(ll)):
        if is_square(ll[i])==False:
            flag = False
            break
    if flag:
        print("NO")
    else:
        print("YES")
        