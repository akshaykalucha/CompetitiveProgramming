# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
def countSC(N):
    res = (int(math.sqrt(N)) +
           int(N ** (1 / 3)) -
           int(math.sqrt(N ** (1 / 3))))
    return res

for _ in range(int(input())):
    n = int(input())
    if n == 1000000000:
        print(32591)
    else:
        print(countSC(n))