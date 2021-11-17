# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    if a%2==0 and b%2!=0 and b>a:
        print(1)
    elif a%2==0 and b%2!=0 and b<a:
        print(2)
    elif a%2==0 and b%2==0 and b>a:
        print(2)
    elif a%2==0 and b%2==0 and b<a:
        print(1)
    elif a%2!=0 and b%2!=0 and a>b:
        print(1)
    elif a%2!=0 and b%2!=0 and b>a:
        print(2)
    elif a%2!=0 and b%2==0 and a>b:
        print(2)
    elif a%2!=0 and b%2==0 and b>a:
        print(1)