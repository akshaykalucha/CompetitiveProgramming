# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
for _ in range(int(input())):
    n = int(input())
    tot = 4*n
    st = []
    while n>0:
        st.append(tot)
        tot-=2
        n-=1
    print(*st)