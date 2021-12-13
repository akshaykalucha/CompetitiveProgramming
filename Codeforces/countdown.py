# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    digs = [int(i) for i in input()]
    minz = sum(digs)
    intdigs = 0
    for el in digs:
        if el > 0:
            intdigs+=1
    if digs[-1]==0:
        print(minz+intdigs)
    else:
        print(minz+intdigs-1)
    