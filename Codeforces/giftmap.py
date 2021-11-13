n=int(input())
l=input().split(' ')
ll=[]
for x in l:
    ll.append(int(x))
i=0
t=1
fl=''
q=True
while t<=n:
    i=0
    while ll[i]!=t:
        i+=1
    else:
        fl+=str(i+1)+' '
    t+=1
print(fl)