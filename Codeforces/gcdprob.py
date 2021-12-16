# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input()) - 1
    if n % 4 == 0:
        print(n // 2 - 1, n // 2 + 1, 1)
    elif n % 2 == 0:
        print(n // 2 - 2, n // 2 + 2, 1)
    else:
        print(n // 2, n // 2 + 1, 1)