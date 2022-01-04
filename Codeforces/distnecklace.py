# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    aa.sort()
    bb.sort()
    ll = []
    mm = []
    for i in range(n):
        ll.append(aa[i])
        mm.append(bb[i])
    print(*ll)
    print(*mm)