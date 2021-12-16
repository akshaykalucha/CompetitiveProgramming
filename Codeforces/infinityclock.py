# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    ll = list(map(int, input().split()))
    if k%2==0:
        k = 2
    else:
        k = 1
    while k > 0:
        zz = max(ll)
        ll = [zz-i for i in ll]
        k -= 1
    print(*ll)