# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, m = map(int, input().split())
    c = 0
    for i in range(1, n+1):
        r = list(input())
        if i<n:
            if r[-1]=='R':
                c+=1
        if i == n:
            c+=r.count('D')
    print(c)