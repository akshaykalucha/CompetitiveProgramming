# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
for _ in range(int(input())):
    n = int(input())
    if n <=30:
        print("NO")
    else:
        print("YES")
        if n == 36 or n == 44 or n == 40:
            print(6,10,15, n-31)
        else:
            print(6,10,14,n-30)