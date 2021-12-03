# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    cc = 0
    for i in range(len(ll)-1):
        zz = max(ll[i],ll[i+1])*min(ll[i],ll[i+1])
        if zz > cc:
            cc = zz
    print(cc)