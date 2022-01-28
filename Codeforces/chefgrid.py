import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    cx=cy=(n+1)//2
    csum = cx+cy
    f = False
    if x+y==csum:
        f = True
    else:
        ss = x+y
        while ss<csum:
            ss+=2
        while ss>csum:
            ss-=2
        if ss==csum:
            f=True
    if f:
        print(0)
    else:
        print(1)