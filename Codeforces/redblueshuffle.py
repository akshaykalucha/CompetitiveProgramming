# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    r = list(input())
    b = list(input())
    redigs = 0
    bluedigs = 0
    for i in range(n):
        if r[i]>b[i]:
            redigs+=1
        elif b[i]>r[i]:
            bluedigs+=1
        if r[i]==b[i]:
            redigs+=1
            bluedigs+=1
    if redigs>bluedigs:
        print("RED")
    elif bluedigs>redigs:
        print("BLUE")
    else:
        print("EQUAL")