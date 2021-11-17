# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    zz = [i for i in range(1,n+1)]
    if n%2==0:
        print(*zz[::-1])
    else:
        mid = (n-1)//2
        zz[mid], zz[mid+1] = zz[mid+1], zz[mid]
        print(*zz[::-1])