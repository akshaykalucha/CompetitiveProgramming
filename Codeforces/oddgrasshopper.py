import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    a,b=map(int,input().split())
    f=b%4
    for i in range(b-f+1,b+1):
        if(a%2==0):
            a-=i
        else:
            a+=i
    print(a)