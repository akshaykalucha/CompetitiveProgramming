import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))[::-1]
    ans = 0
    prev = -1
    big = max(ll)
    for x in ll:
        if x==big:
            break
        if x < big and x > prev:
            ans+=1
            prev = x
        if x > prev:
            prev = x
    print(ans)