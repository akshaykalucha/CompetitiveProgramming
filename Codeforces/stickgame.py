# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


a, b = map(int, input().split())
 
if a // b % 2 != 0:
    print('Yes')
else:
    print('NO')