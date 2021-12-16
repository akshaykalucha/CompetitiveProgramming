# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, s = map(int, input().split())
rem = s%n
if rem == 0:
    print(s//n)
else:
    print(((s-rem)//n) + 1)
