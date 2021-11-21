# import sys
# sys.stdin = open('Codeforces/input.txt', 'r')
# sys.stdout = open('Codeforces/output.txt', 'w')

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    curr = 0
    while a+b<=n:
        if a < b:
            a+=b
        else:
            b+=a
        curr+=1
    print(curr+1)