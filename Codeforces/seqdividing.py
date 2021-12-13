# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
if n%2==0:
    if (n//2)%2==0:
        print(0)
    else:
        print(1)
else:
    if ((n+1)//2)%2==0:
        print(0)
    else:
        print(1)