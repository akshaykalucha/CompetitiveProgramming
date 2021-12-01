# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


def solve():
    a,b,c = map(int,input().split())
    s = [a,b,c]
    if a>b and a>c:
        a1 = 0
    else:
        a1 = max(s)+1-a
    if b>a and b>c:
        b1 = 0
    else:
        b1 = max(s)+1-b
    if c>b and c>a:
        c1 = 0
    else:
        c1 = max(s)+1-c
    print(a1,b1,c1)
 
 
t = int(input())
for _ in range(t):
    solve()