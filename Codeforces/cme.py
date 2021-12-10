# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(2)
    elif n == 1:
        print(3)
    else:
        if n%2==0:
            print(0)
        else:
            print(1)