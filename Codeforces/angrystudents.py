# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(input())
    tt = 0
    ct = 0
    afound = False
    for i in range(len(ll)):
        if ll[i]=='A':
            afound = True
        if ll[i]=="P" and afound==True:
            ct+=1
        else:
            if ct > tt:
                tt = ct
                ct = 0
            else:
                ct=0
        if i == len(ll)-1:
            if ct > tt:
                tt=ct
    print(tt)
            