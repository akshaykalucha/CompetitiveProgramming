# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n = int(input())
if n%2==0:
    print(n//2)
    print(*["2"]*(n//2))
else:
    newz = n-3
    print((newz//2)+1)
    print(3,*["2"]*(newz//2))