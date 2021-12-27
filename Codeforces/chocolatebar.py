# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
for _ in range(int(input())):
    s,a,b,c = map(int, input().split())
    bars = (math.floor(s//c))
    rem = s%a
    s-=rem
    if bars>=a:
        bars+=((bars//a)*b)
    print(bars)