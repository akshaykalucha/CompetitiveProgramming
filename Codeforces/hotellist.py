# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n=int(input())
x=input()
y=[0,0,0,0,0,0,0,0,0,0]
ans=""
for i in range(len(x)):
    if x[i]=='L':
        for j in range(len(y)):
            if y[j]==0:
                y[j]=1
                break
    elif x[i]=='R':
        for j in range(len(y)-1,-1,-1):
            if y[j]==0:
                y[j]=1
                break
    else:
        a=x[i]
        y[int(a)]=0
print(*y,sep='')
