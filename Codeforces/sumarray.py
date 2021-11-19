# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
    if n == 2:
        print(m)
    else:
        if n > 2:
            print(m*2)