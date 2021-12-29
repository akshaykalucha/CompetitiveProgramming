# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

a,b,c = map(int, input().split())
if a==b:
    print(2*c+(a+b))
else:
    print(2*c+(min(a,b)*2)+1)