# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    c= int(input())
    r1 = []
    r2 = []
    f = True
    for i in range(2):
        row = list(input())
        if i==0:
            r1 = row
        else:
            r2 = row
    for i in range(c):
        if r1[i]==r2[i]=="1":
            print("NO")
            f = False
            break
    if f:
        print("YES")