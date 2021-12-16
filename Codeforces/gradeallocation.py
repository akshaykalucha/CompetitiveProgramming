# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n, m = map(int, input().split())
    ll = list(map(int, input().split()))
    tot = sum(ll)
    if tot>=m:
        print(m)
    else:
        print(tot)
        