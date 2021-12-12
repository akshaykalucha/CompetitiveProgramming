# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n,x=map(int, input().split())
    ll = list(map(int, input().split()))
    curr = 0
    if sum(ll)==x:
        print("NO")
    else:
        print("YES")
        for i in range(n-1):
            if curr+ll[i]==x:
                ll[i],ll[i+1]=ll[i+1],ll[i]
            curr+=ll[i]
        print(*ll)