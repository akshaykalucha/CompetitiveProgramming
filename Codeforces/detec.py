# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')
for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    zz = set(ll)
    for el in zz:
        if ll.count(el) == 1:
            print(ll.index(el)+1)
            break