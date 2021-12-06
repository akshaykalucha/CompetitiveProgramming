# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    else:
        if n>=6:
            if n%2==0:
                print(2)
            else:
                print(3)
        else:
            if n==2:
                print(1)
            elif n==3:
                print(2)
            elif n==4:
                print(2)
            elif n==5:
                print(3)