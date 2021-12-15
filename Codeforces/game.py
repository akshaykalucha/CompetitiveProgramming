# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n1,n2,k1,k2 = map(int, input().split())

if n1 > n2:
    print("First")
elif n2>n1:
    print("Second")
elif n1==n2:
    if k1<k2:
        print("Second")
    elif k2<k1:
        print("Second")
    elif k1==k2:
        print("Second")