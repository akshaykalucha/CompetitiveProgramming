# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    cc = 0
    zz = set(ll)
    for el in zz:
        if ll.count(el) > cc:
            cc = ll.count(el)
    print(cc)