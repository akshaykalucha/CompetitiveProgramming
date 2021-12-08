# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    ll.sort()
    zz = []
    end = []
    for i in range(len(ll)):
        if i == 0:
            zz.append(ll[i])
        else:
            if zz[-1]==ll[i]:
                end.append(ll[i])
            else:
                zz.append(ll[i])
    print(*zz, end=" ")
    print(*end[::-1])