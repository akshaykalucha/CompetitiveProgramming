# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
import math
n = int(input())
i = 0
s1=["."]*n
coubt = 0
while i<=(n-1):
    s1[i]="C"
    coubt+=1
    i+=2
s2 = ["."]*n
i=1
while i<=(n-1):
    s2[i]="C"
    coubt+=1
    i+=2
f=True
print(math.ceil((n*n)/2))
for i in range(n):
    if f:
        print("".join(s1))
        f=False
    else:
        print("".join(s2))
        f=True