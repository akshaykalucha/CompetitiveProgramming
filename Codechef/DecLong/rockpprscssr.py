import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    s = list(input())
    sind = 0
    rind = 0
    pind = 0
    c = []
    for i in range(len(s)-1, 0, -1):
        if s[i]=='S':
            sind = i
            break
    for i in range(len(s)-1, 0, -1):
        if s[i]=='R':
            rind = i
            break
    for i in range(len(s)-1, 0, -1):
        if s[i]=='P':
            pind = i
            break
    for i in range(len(s)):
        if s[i]=="R":
            if pind>i:
                if sind>pind:
                    if rind>sind:
                        c.append("R")
                    else:
                        c.append("S")
                else:
                    c.append("P")
            else:
                c.append("R")
        elif s[i]=='P':
            if sind>i:
                if rind>sind:
                    if pind>rind:
                        c.append("P")
                    else:
                        c.append("R")
                else:
                    c.append("S")
            else:
                c.append("P")
        elif s[i]=="S":
            if rind>sind:
                if pind>rind:
                    if sind>pind:
                        c.append("S")
                    else:
                        c.append("P")
                else:
                    c.append("R")
            else:
                c.append("S")
    # print(rind, pind, sind)
    print("".join(c))