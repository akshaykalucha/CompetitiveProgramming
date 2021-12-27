# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
*v,d=map(int,input().split());a,b,c=sorted(v);print(max(0,d-b+a)+max(0,d-c+b))