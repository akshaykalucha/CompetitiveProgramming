# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    eve = []
    odd = []
    for i in range(len(ll)):
        if ll[i]%2==0:
            eve.append(ll[i])
        else:
            odd.append(ll[i])
    print(*odd,*eve)