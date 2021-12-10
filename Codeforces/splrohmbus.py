# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


def solve(n):
    if n == 1:
        return 1
    else:
        return ((n-1)*4) + solve(n-1)
n = int(input())
print(solve(n))