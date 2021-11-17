# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

cals = list(map(int, input().split()))
gm = input()
c = 0
for i in range(len(gm)):
    if gm[i]=="1":
        c+=cals[0]
    elif gm[i]=="2":
        c+=cals[1]
    elif gm[i]=="3":
        c+=cals[2]
    elif gm[i]=="4":
        c+=cals[3]
print(c)