p=[1,4,-1]
for sasasdfds in range(int(input())):
    n=int(input())
    l=[]
    r=[]
    if n%4!=0:
        print('NO')
    else:
        print('YES')
        for i in range(2, n+1, 2):
            l.append(i)
            r.append(i-1)
        r[-1]+=l[-1]-len(l)
        print(*l,*r)