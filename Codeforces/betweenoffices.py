# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
ll = list(input())
se = 0
sf = 0

for i in range(len(ll)-1):
    if ll[i]=='S' and ll[i+1]=="F":
        sf+=1
    elif ll[i]=='F' and ll[i+1]=="S":
        se+=1
if sf>se:
    print("YES")
else:
    print("NO")