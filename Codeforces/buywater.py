# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    a2 = 2*a
    cost = 0
    if n%2==0:
        if b<a2:
            cost = (n//2)*b
        elif b==a2:
            cost = (n//2)*b
        elif b>a2:
            cost = n*a
    if n%2!=0:
        if b<a2:
            cost = (((n-1)//2)*b)+a
        elif b>a2:
            cost = (((n-1)//2)*a2)+a
        elif b==a2:
            cost = (((n-1)//2)*a2)+a
    print(cost)