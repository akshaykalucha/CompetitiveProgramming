# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    if sum(ll)/n == 1:
        print(0)
    else:
        if sum(ll) > 0:
            if sum(ll)-n > 0:
                print(sum(ll)-n)
            else:
                print(1)
        elif sum(ll) <= 0:
            print(1)