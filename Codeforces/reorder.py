# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, m = map(int, input().split())
    ll = list(map(int, input().split()))
    if sum(ll)==m:
        print("YES")
    else:
        print("NO")