# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] + a[1] <= a[n-1]:
        print(1, 2, n)
    else:
        print(-1)