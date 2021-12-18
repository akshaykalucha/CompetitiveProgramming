# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

t = int(input())
while t>0:
    t = t-1
    a,b = map(int,input().split())
    if a == b: 
        if a>0:
            print(1)
        else:
            print(0)
    elif ((a - b) % 2 != 0): 
        print(-1)
    else:
        print(2)