# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    val = sum(li)
    print(math.ceil(val/n))