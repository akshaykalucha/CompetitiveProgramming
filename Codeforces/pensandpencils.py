# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    a,b,c,d,k = map(int, input().split())
    tot = 0
    pens = 0
    pencils = 0
    if c<=a:
        rem = a%c
        a-=rem
        if rem>0:
            tot+=(a//c)+1
            pens+=(a//c)+1
        else:
            tot+=(a//c)
            pens+=(a//c)          
    elif a<c:
        tot+=1
        pens+=1
    if d>=b:
        tot+=1
        pencils+=1
    elif b>d:
        rem = b%d
        b-=rem
        if rem>0:
            tot+=(b//d)+1
            pencils+=(b//d)+1
        else:
            tot+=(b//d)
            pencils+=(b//d)
    if tot>k:
        print(-1)
    else:
        print(pens, pencils)