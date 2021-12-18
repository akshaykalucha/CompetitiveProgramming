# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

consc = []
n = int(input())
ll = list(input())
cmax = 0
for i in range(n):
    if ll[i]=="B":
        cmax+=1
    if ll[i]=='W':
        if cmax>0:
            consc.append(cmax)
            cmax=0
    if i==(n-1) and cmax>0:
        consc.append(cmax)
print(len(consc))
print(*consc)