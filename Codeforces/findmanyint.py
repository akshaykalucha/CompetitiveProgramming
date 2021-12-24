# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

x = int(input())
init = False
for a in range(1, x+1):
    f = False
    for b in range(1, x+1):
        if a%b==0 and a*b>x and a//b<x:
            print(a,b)
            f = True
            init = True
            break
    if f:
        break
if init==False:
    print(-1)