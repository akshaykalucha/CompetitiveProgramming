import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')
for _ in range(int(input())):
    n = int(input())
    cmin = 9999999999
    cmax = -1
    cost = []
    for i in range(n):
        li,ri,ci = map(int, input().split())
        if i == 0:
            print(ci)
            cmin = min(li,cmin)
            cmax = max(ri,cmax)
            cost.sppend()
        else:
            if li<cmin or ri>cmax:
                