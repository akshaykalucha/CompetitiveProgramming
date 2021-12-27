# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
n = int(input())
m = int(input())
cc = 0
ss = 0
ll = []

for i in range(n):
    ai = int(input())
    ll.append(ai)
ll.sort(reverse=True)
for i in range(n):
    if m>0:
        m-=ll[i]
        cc+=1
    else:
        break
print(cc)