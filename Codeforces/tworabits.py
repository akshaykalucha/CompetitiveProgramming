# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    x,y,a,b=map(int, input().split())
    dist = y-x
    hop = a+b
    if dist%hop==0:
        print(dist//hop)
    else:
        print(-1)