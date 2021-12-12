# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    dead = False
    height = 1
    prev = 0
    for i in range(len(ll)):
        if i == 0:
            if ll[i]==1:
                height+=1
        else:
            if ll[i]==1 and ll[i-1]==1:
                height+=5
            elif ll[i]==1 and ll[i-1]==0:
                height+=1
            elif ll[i]==0 and ll[i-1]==0:
                dead = True
                break
    if dead:
        print(-1)
    else:
        print(height)