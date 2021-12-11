# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    c = 0
    for i in range(len(ll)):
        if ll[i]==0:
            c+=1
            ll[i]=1
    if sum(ll)==0:
        ll[0]=1
        c+=1
    print(c)
    