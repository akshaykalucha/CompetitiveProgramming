# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int,input().split()))
    if min(ll)<0:
        print("No")
    else:
        print("YES")
        print(101)
        print(*[i for i in range(0,101)])