# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    win = 0
    z = min(ll)
    for i in range(len(ll)):
        if ll[i] > z:
            win+=1
    print(win)