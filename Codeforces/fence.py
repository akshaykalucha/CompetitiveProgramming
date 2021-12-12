# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for i in range(int(input())):
    a, b, c = sorted(list(map(int,input().split())))
    print(c-b+1)