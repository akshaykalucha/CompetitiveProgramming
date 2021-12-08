# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    ll = list(map(int, input().split()))
    cur = 0
    while k>0 and cur<n-1:
        if ll[cur]==0 :
            cur+=1
        else:
            ll[cur]-=1
            ll[-1]+=1
            k-=1
    print(*ll)
        