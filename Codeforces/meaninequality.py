# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    kk = []
    ll.sort(reverse=True)
    for i in range(n):
        kk.append(ll[i])
        kk.append(ll[-1])
        ll.pop()
    print(*kk)