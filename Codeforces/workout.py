# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))

chest = 0
bicep = 0
back = 0
curr = 1
for i in range(n):
    if curr==1:
        chest+=ll[i]
        curr=2
    elif curr==2:
        bicep+=ll[i]
        curr=3
    else:
        back+=ll[i]
        curr=1

if chest > back and chest > bicep:
    print("chest")
elif back > chest and back > bicep:
    print("back")
else:
    print("biceps")