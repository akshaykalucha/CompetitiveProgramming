# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    o = []
    e = []
    for i in range(len(ll)):
        if ll[i]%2==0:
            e.append(i+1)
        else:
            o.append(i+1)
    if len(e)>=1:
        print(1)
        print(e[0])
    elif len(o)>=2:
        print(2)
        print(o[0], o[1])
    else:
        print(-1)