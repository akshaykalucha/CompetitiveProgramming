# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    palin = "a"*k
    oth = ""
    n -= k
    while n>=3:
        oth += "cba"
        n-=3
    if n < 3:
        oth += "cba"[:n]
    print(palin+oth)