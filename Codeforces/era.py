# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    inc = 0
    for i in range(len(ll)):
        ind = i+1
        if ll[i]>(ind+inc):
            inc+=(ll[i]-(ind+inc))
    print(inc)