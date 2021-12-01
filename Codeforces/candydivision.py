# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    ll = list(map(int, input().split()))
    if sum(ll)%2==0:
        print(sum(ll)//2)
    else:
        print((sum(ll)-1)//2)