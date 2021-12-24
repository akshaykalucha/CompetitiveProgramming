import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    dic = {}
    if n==1:
        print(1)
        print(1,1)
    elif n==2:
        print(2)
        print(3,1)
        print(4,1)
    elif n==4:
        print(1)
        print(1,4)
    else:
        print(2)
        print(2,n-1)  
        print(n-2,1) 