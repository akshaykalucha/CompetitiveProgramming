# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
if n%3==0:
    print(1,1,n-2)
elif n%3==1:
    print(1,1,n-2)
else:
    print(2,2,n-4)