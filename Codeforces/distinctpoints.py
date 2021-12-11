# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    l1,r1,l2,r2=map(int, input().split())
    z = 0
    if l1!=l2:
        z=l2
    elif l1!=r2:
        z=r2
    print(l1,z)