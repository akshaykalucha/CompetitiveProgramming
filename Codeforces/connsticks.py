# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        print(n//2)
    else:
        print(((n-1)//2)+1)