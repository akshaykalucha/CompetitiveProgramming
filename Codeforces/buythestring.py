# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n,c0,c1,h = map(int, input().split())
    ll = list(input())
    s0 = ll.count("0")
    s1 = ll.count("1")
    origprc = (s0*c0) + (s1*c1)
    flag = False
    if c0 > c1 and h < c0:
        cost = (s0*h)+(s0*c1)+(s1*c1)
        if cost < origprc:
            origprc = cost
        # newpr = s1*c1
        # while newpr < origprc and s0 > 0:
        #     newpr+=h
        #     newpr+=c1
        #     s0-=1
        # flag = True
        # newpr+=s0*c0
    elif c1>c0 and h < c1:
        cost = (s1*h)+(s1*c0)+(s0*c0)
        if cost < origprc:
            origprc = cost
        # newpr = s0*c0
        # while newpr < origprc and s1>0:
        #     newpr+=h
        #     newpr+=c0
        #     s1-=1
        # flag = True
        # newpr+=(s1*c1)
    print(origprc)