n, t = map(int, input().split())
ss = input()
z = [0]*n
for i in range(len(ss)):
    if ss[i]=='G':
        z[i]=1
for i in range(t):
    vis = None
    for j in range(len(z)-1):
        if z[j]==0 and z[j+1]==1 and j-1!=vis:
            z[j]=1
            z[j+1]=0
            vis=j
s=""
for i in range(len(z)):
    if z[i]==1:
        s+='G'
    else:
        s+='B'
print(s)