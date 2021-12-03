# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    r, b, d = map(int, input().split())
    flag = True
    if abs(r-b)/min(r,b)<=d:
        print('YES')
    else:
        print("NO")