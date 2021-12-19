# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    if n<=7:
        print(1)
    else:
        rem = n%7
        n-=rem
        print((n//7)+1)