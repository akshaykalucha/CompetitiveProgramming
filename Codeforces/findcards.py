# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

import math
n, x = map(int, input().split())
ll = list(map(int, input().split()))
cs = abs(sum(ll))
print(math.ceil(cs/x))