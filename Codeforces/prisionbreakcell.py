# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


t = int(input())
while(t):
    n,m,r,c = map(int, input().split())
    print(max(n-r,r-1) + max(m-c,c-1))
    t-=1

for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    c1 = c-1
    c2 = m-c
    r1 = r-1
    r2 = n-r
    print(max([c1+r1,c2+r2]))