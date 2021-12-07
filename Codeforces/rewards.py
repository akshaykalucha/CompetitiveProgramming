# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
import math
a1,a2,a3 = [int(i) for i in input().split()]
a = a1+a2+a3
b1,b2,b3 = [int(i) for i in input().split()]
b = b1+b2+b3
n = int(input())
a = a/5
a = math.ceil(a)
b = b/10
b = math.ceil(b)
shelf = a + b
if n >= shelf:
    print("YES")
else:
    print("NO")