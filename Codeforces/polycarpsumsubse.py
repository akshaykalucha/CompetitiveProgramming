# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    b = list(map(int, input().split()))
    if b[0]+b[1]==b[2]:
        print(b[0],b[1],b[3])
    else:
        print(b[0],b[1],b[2])