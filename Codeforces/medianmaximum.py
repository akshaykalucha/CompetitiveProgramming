# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

from math import ceil
for _ in range(int(input())):
    n,s=map(int,input().split())
    remove=ceil(n/2)-1
    n=n-remove
    print(s//n)