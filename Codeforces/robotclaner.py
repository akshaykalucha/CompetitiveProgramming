# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, m, rb,cb,rd,cd = map(int, input().split())
    dr=1
    dc=1
    t = 0 
    
    while True:
        if rb==rd or cb==cd:
            break
        if dr==1 and rb==n:
            dr = -1
        elif dr==-1 and rb==1:
            dr=1
        if dc==1 and cb==m:
            dc=-1
        elif dc==-1 and cb==1:
            dc=1
        rb+=dr
        cb+=dc
        t+=1
    print(t)