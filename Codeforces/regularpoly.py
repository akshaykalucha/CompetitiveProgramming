# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    m, n = map(int, input().split())
    if m%n==0:
        print("YES")
    else:
        print("NO")