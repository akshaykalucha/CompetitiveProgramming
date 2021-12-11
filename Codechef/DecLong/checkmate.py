import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    kx,ky=map(int, input().split())
    x1,y1 = map(int, input().split())
    x2,y2=map(int, input().split())
    ans = "NO"
    corner = False
    if kx==1 or ky==1 or kx==8 or ky==8:
        corner = True
    if corner:
        if kx==1:
            if x1==2 or x2==2 and y1!=y2:
                if (abs(y1-ky)>1) and (abs(y2-ky)>1):
                    ans="YES"
        if kx==8:
            if x1==7 or x2==7 and y1!=y2:
                if (abs(y1-ky)>1) and (abs(y2-ky)>1):
                    ans="YES"
        if ky==1:
            if y1==2 or y2==2 and x1!=x2:
                if (abs(x1-kx)>1) and (abs(x2-kx)>1):
                    ans="YES"
        if ky==8:
            if y1==7 or y2==7 and x1!=x2:
                if (abs(x1-kx)>1) and (abs(x2-kx)>1):
                    ans="YES"
    print(ans)