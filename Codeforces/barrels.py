# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    ll = list(map(int, input().split()))
    ll.sort()
    i = n-2
    while k>0 and i>=0:
        ll[-1]+=ll[i]
        i-=1
        k-=1
    print(ll[-1])