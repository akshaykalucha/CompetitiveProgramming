# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    xx = list(map(int, input().split()))
    yy = list(map(int, input().split()))
    xx.sort()
    yy.sort()
    while len(xx)>0 and len(yy)>0:
        if xx[-1]>yy[-1]:
            xx.append(yy[-1])
            xx.sort()
            yy.pop()
        else:
            yy.append(xx[-1])
            yy.sort()
            xx.pop()
    if len(xx)==0:
        print("NO")
    else:
        print("YES")