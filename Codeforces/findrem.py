# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    x, y, n = map(int, input().split())
    d = (n-y)//x
    print(x*d+y)