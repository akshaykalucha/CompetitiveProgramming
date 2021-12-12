# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    if len(set(ll))==1:
        print(len(ll))
    else:
        print(1)