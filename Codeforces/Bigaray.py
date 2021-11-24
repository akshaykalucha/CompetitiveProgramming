# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    c = 0
    ll.sort()
    while True:
        if ll[-1] > (ll[0]+ll[-1])/2:
            ll.pop()
            c += 1
        else:
            break
    print(c)